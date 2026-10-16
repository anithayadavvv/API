from fastapi import FastAPI, HTTPException
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

@app.get("/students/{student_id}")
def get_student(student_id: int):
    students = [
        {"id": 1, "name": "Aarav", "age": 17},
        {"id": 2, "name": "Rebecca", "age": 17},
        {"id": 3, "name": "Sameera", "age": 18},
        {"id": 4, "name": "Anitha", "age": 17}
    ]
    for student in students:
        if student["id"] == student_id:
            return student 

    raise HTTPException(
        status_code=404,
        detail="Dumdahh there ain't no student like that",
    )

