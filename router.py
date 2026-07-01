from models import Student
from fastapi import APIRouter,status

# Initialize the router instance
router = APIRouter()
students = {}



@router.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student:Student):
    students[student.matric_number] = student
    return {"message": "Student created successfully", "student": student}

@router.get("/students/{matric_number}")
def get_student(matric_number: str): 
   if students.get(matric_number) is None:
        return {"message": "Student not found"}  
   return students[matric_number]

@router.get("/students")
def get_all_students():
    return students

@router.put("/students/{matric_number}")
def update_student(matric_number: str, student: Student):   
    if students.get(matric_number) is None:
        return {"message": "Student not found"}
    students[matric_number] = student
    return {"message": "Student updated successfully", "student": student}

@router.delete("/students/{matric_number}")
def delete_student(matric_number: str):
    if students.get(matric_number) is None:
        return {"message": "Student not found"}
    del students[matric_number]
    return {"message": "Student deleted successfully"}