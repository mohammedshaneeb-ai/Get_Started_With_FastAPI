from fastapi import FastAPI
from pydantic import BaseModel
from utils import generate_description

class Order(BaseModel):
    product : str
    units : int

class Product(BaseModel):
    name : str
    notes : str

app = FastAPI()

@app.get('/welcome')
async def welcome():
    return {'message':"Welcome to AI World"}

@app.get('/hello')
async def hello_world():
    return {'message':"Hello World"}

@app.post('/orders')
async def place_order(product:str, units:int):
    return {'message':f"Order for {units} units of {product} placed succesfully"}

@app.post('/order_pydantic')
async def order_pydantic(order:Order):
    return {'message':f"Order for {order.units} units of {order.product} placed Succesfully"}

@app.post('/generate_desc')
async def generate_prdct_description(product:Product):
    description = generate_description(f"Product name :{product.name} , Notes:{product.notes}")
    return {'description':description}



    