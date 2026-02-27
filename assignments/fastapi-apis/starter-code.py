from fastapi import FastAPI

app = FastAPI()

# In-memory store for demonstration
items = []

@app.get("/items")
def list_items():
    return items

@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return item

# Additional endpoints can be added by students
