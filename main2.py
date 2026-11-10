import fastapi
from dummydata import items

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return "HEMA ENTERPRISES"

@app.get("/contact")
def contact():
    return " You can connect us on watsapp !! 70......08 "

@app.get("/products")
def product():
    return items

## Path Paras:::
@app.get("/product/{product_id}")
def singleproduct(product_id:int):
    return(

    )