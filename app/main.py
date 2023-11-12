from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to the open-med-calc API. Please see the documentation at http://openmedcalc.org/api/docs for more information" }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}



