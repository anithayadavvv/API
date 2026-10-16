# Student API 🚀

A beginner-friendly REST API built with **Python** and **FastAPI** while learning backend development.

## Features

- Retrieve all students
- Retrieve a student by ID
- Filter students by age
- Return appropriate HTTP errors when a student isn't found
- Interactive API documentation with Swagger UI

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Git and GitHub

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/anithayadavvv/API.git
cd API
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
cd student-api
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install fastapi uvicorn
```

### 4. Run the API

```powershell
python -m uvicorn main:app --reload
```

### 5. Explore the API

With the server running, open:

- **API root:** http://127.0.0.1:8000/
- **All students:** http://127.0.0.1:8000/students
- **Filter by age:** http://127.0.0.1:8000/students?student_age=17
- **Get a student by ID:** http://127.0.0.1:8000/students/1
- **Interactive documentation:** http://127.0.0.1:8000/docs

## What I'm Learning

This project is part of my journey toward becoming a backend engineer. I'm learning REST APIs, HTTP methods, JSON, request handling, error handling, and API development with FastAPI.

## Project Status

Actively learning and improving. More features will be added as the project develops.
