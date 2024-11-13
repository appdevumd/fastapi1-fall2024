from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# this will hold the items
todo_list_items = []
class Item(BaseModel):
    name: str
    description: str
    is_done: bool
    deadline: str

class ItemToRemove(BaseModel):
    index: int

"""
/v1/auth/login
/v2/auth/signup
/app/items - GET
/app/add - POST


"""

@app.get('/items')
async def root():
    return {'items': todo_list_items}

@app.post('/add')
async def add_element(item: Item):
    todo_list_items.append(item)
    return {'message': 'successfully added'}

@app.delete('/remove')
async def remove_element(item: ItemToRemove):
    todo_list_items.pop(item.index)
    return {'message': 'success'}
