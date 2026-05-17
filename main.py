from fastapi import FastAPI

# need a app object which is object of fastapi:
app = FastAPI()

# defining route/path for our endpoint:
@app.get("/")
def hello():
    return {'message':'Hello i am Himanshu'}

@app.get("/about")
def about():
    return {'message':"MCA student looking for AI role"}