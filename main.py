from fastapi import FastAPI  #from fastapi package import FastAPI class
app=FastAPI()  #app is an object of FastAPI class
@app.get("/")
def home():
    return {"message":"welcome to student API"}