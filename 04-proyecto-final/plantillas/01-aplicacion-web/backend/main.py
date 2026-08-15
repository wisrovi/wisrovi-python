"""Backend API con FastAPI."""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Web App Template", version="1.0.0")

class Item(BaseModel):
    nombre: str
    precio: float

items_db = []

@app.get("/items")
def get_items():
    return {"items": items_db}

@app.post("/items")
def add_item(item: Item):
    items_db.append(item.model_dump())
    return {"mensaje": "Agregado", "item": item}
