from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "The API is running"}


@app.get("/students")
def get_students():
    return [
        {"id": 1, "name": "Aarav", "age": 17},
        {"id": 2, "name": "Rebecca", "age": 17},
        {"id": 3, "name": "Sameera", "age": 18},
        {"id": 4, "name": "Anitha", "age": 17}
    ]

