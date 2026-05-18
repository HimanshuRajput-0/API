from fastapi import FastAPI, Path, HTTPException
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

# getting specific data using path parameters:
@app.get('/person/{person_id}')
def view_person(person_id = Path(..., description='id of the person in the db', example='01')):
    #load full data:
    data = load_data()

    # find the required data:
    if person_id in data:
        return data[person_id]
    raise HTTPException(status_code=404, detail = 'Person not found')