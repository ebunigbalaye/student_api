from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from database import Student as DatabaseStudent
from models import StudentSchema,StudentUpdate  # Pydantic schema


router = APIRouter()




@router.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: StudentSchema, db: Session = Depends(get_db)):

    db_student = DatabaseStudent(
        name=student.name,
        matric_number=student.matric_number,
        age=student.age,
        cgpa=student.cgpa,
        faculty=student.faculty,
        date_of_birth=student.date_of_birth)

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return { "message": "Student created successfully", "student": db_student}


@router.get("/students/{matric_number}")
def get_student(matric_number: str, db: Session = Depends(get_db)):
    student = db.query(DatabaseStudent).filter(DatabaseStudent.matric_number == matric_number).first()

    if not student:
        raise HTTPException(status_code=404,detail="Student not found")

    return student


@router.get("/students")
def get_all_students(db: Session = Depends(get_db)):
    students = db.query(DatabaseStudent).all()
    return students



@router.patch("/students/{matric_number}")
def update_user( matric_number: str,student: StudentUpdate,db: Session = Depends(get_db)):
    # 1. Fetch the existing record from the database
    db_student = db.query(DatabaseStudent).filter(DatabaseStudent.matric_number == matric_number).first()
    if not db_student: 
        raise HTTPException(status_code=404, detail="Student not found")
    
    # 2. Extract ONLY the fields explicitly provided by the client
    update_data = student.model_dump(exclude_unset=True)
    
    # 3. Dynamically apply updates to the database model
    for key, value in update_data.items():
        setattr(db_student, key, value)
        
    # 4. Save changes and return the fresh database state
    db.commit()
    db.refresh(db_student)
    return db_student

@router.delete("/students/{matric_number}")
def delete_student(matric_number: str, db: Session = Depends(get_db)):

    db_student = db.query(DatabaseStudent).filter(
        DatabaseStudent.matric_number == matric_number
    ).first()

    if not db_student:
        raise HTTPException(status_code=404,detail="Student not found")

    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted successfully"}