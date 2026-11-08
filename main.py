# from fastapi import FastAPI, HTTPException #from fastapi package import FastAPI class
# from pydantic import BaseModel # pydantic validates the info recieved from the api

# app=FastAPI()  #app is an object of FastAPI class

# @app.get("/")  #.get() Defines an API that handles GET requests
#                # / the url path (endpoint)
#                # when someone sends a request to this url fastAPI excetues home function
# def home():
#     return {"message":"welcome to student API"}

# @app.get("/student") # This endpoint returns student information whenever someone sends a GET request to /student
# def get_student():
#     return{
#         "name":"Rochana",
#         "course":"MCA",
#         "college":"IMCC"
#     }

# class Student(BaseModel):
#     name:str
#     course:str
#     college:str

# @app.post("/student")
# def add_student(student:Student):
#     return{
#         "message": "student added successfully",
#         "student": student
#     }

from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

students={
    1:{
        "name":"Rochana",
        "college":"MMCC",
        "course":"BBA(CA)"
    }
}

class Student(BaseModel):
    name:str
    college:str
    course:str

@app.put("/student/{student_id}") #url contains dynamic student id
def put_request(student_id:int, student:Student):  #Receives the student's ID   Receives and validates student details
    students[student_id]=student.model_dump()  #Finds that student's record   Converts student data into a dictionary

    return{"message":"student record succesfully updated using put method"}


@app.get("/student")
def display():
    return students