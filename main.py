from fastapi import FastAPI

app=FastAPI()

@app.get("/{id}")
def hello_world(id: int, name: str, dob: int):
 return {"id": id, "name": name, "Date of Birth": dob}

@app.get("/hello")
def hello_world_2():
 return {"hello": "world2"}



