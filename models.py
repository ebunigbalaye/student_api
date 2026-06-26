from datetime import date
from enum import Enum
from pydantic import BaseModel

class Faculty(Enum):
    SIMME = "SIMME"
    SESE = "SESE"
    SOC = "SOC"
    SAAT = "SAAT"
    SET="SET"
    SEMS="SEMS"

class Student(BaseModel):
    matric_number: str
    name: str
    date_of_birth: date
    age: int
    faculty: Faculty
    cgpa: float