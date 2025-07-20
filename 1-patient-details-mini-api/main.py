from fastapi import FastAPI
import json

app = FastAPI() # creat object of FastAPI
def load_data():
    with open('patients.json', 'r') as file:
        return json.load(file)


@app.get("/")  # define a (/) route or path get request & it called npoint
def hello():  
    return {'message': "Patient Management System API."}

@app.get("/about") # it is another npoint 
def about():
    return {'message': "A fully functional API for managing patient records."}

@app.get('/view')
def view():
    data = load_data()
    return data










# run command in terminal : uvicorn main:app --reload
# this command will start the server and you can access the API at http://127.0
# http://127.0/docs will give you the documentation of the API
# http://127.0/openapi.json will give you the openapi schema of the API