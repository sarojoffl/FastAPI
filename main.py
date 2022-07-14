from fastapi import FastAPI

app=FastAPI()

movies = {
         1:{
            "name": "Fight Club",
            "rating": 10,
            "year": 1999,
           },

         17:{
            "name": "Intersteller",
            "rating": 10,
            "year": 2014,
           }
         }

@app.get("/movies")
def get_all_movies():
 return {"data": movies}

@app.get("/movie/{id}")
def get_movie_by_id(id: int):
 return {"data": movies[id]}

@app.post("/movie")
def add_movie(id: int, name: str, rating:int, year:int):
 new_movie = {id: {"name": name, "rating": rating, "year": year}}
 movies.update(new_movie)
 return {"data": new_movie, "message": "Update successfully"}

@app.put("/movie/{id}")
def update_movie_by_id(id:int, name: str, rating: int, year: int):
 movies[id] = {"name": name, "rating": rating, "year": year}
 return {"message": "Movie updated", "data": f"movies[{id}]"}
