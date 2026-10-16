from fastapi import FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()
@app.get("/")
def home():
    return {"message": "The API is running"}

students = [
    {"id": 1, "name": "Aarav", "age": 17},
    {"id": 2, "name": "Rebecca", "age": 17},
    {"id": 3, "name": "Sameera", "age": 18},
    {"id": 4, "name": "Anitha", "age": 17},
]


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return JSONResponse(status_code=404, content={"message": "Student not found"})