from fastapi import FastAPI

app = FastAPI()

data_store = {}  # Simple in-memory store


@app.get("/something/{id}")
def get_something(index: int):
    if index in data_store:
        return {"index": index, "value": data_store[index]}
    return {"error": "Item not found"}


@app.delete("/something/{id}")
def delete_something(index: int):
    if index in data_store:
        del data_store[index]
        return {"message": "Item deleted", "index": index}
    return {"error": "Item not found"}


@app.post("/something/{id}")
def create_something(index: int, value: str):
    if index in data_store:
        return {"error": "Item already exists"}
    data_store[index] = value
    return {"message": "Item created", "index": index, "value": value}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
