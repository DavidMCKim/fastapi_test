from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name : str
    description : str = None
    price : float
    tax : float = None

app = FastAPI()

@app.get('/')
async def root():
    return { 'message' : 'Hello World' }

@app.post('/Items/')
async def create_item(item : Item):
    return item

@app.get("/book/{item_id}")
async def read_item(item_id):
    return {"book": item_id}