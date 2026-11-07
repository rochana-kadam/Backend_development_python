from fastapi import FastAPI  #from fastapi package import FastAPI class
from pydantic import BaseModel # pydantic validates the info recieved from the api

app=FastAPI()  #app is an object of FastAPI class

@app.get("/")  #.get() Defines an API that handles GET requests
               # / the url path (endpoint)
               # when someone sends a request to this url fastAPI excetues home function
def home():
    return {"message":"welcome to student API"}

@app.get("/student") # This endpoint returns student information whenever someone sends a GET request to /student
def get_student():
    return{
        "name":"Rochana",
        "course":"MCA",
        "college":"IMCC"
    }

class Student(BaseModel):
    name:str
    course:str
    college:str

@app.post("/student")
def add_student(student:Student):
    return{
        "message": "student added successfully",
        "student": student
    }