from fastapi import FastAPI
import json

# need a app object which is object of fastapi:
app = FastAPI()

# Supporting function for Data Loding:
def load_data():
    with open("Info.json", 'r') as f:
        data = json.load(f)

    return data

# defining route/path for our endpoint:
@app.get("/")
def hello():
    return {'message':'Hello i am Himanshu'}

@app.get("/about")
def about():
    return {'message':"MCA student looking for AI role"}

@app.get("/view")
def view():
    data = load_data()

    return data