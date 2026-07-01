from datetime import date
from enum import Enum
from pydantic import BaseModel
from typing import Optional


class Faculty(Enum):
    SIMME = "SIMME"
    SESE = "SESE"
    SOC = "SOC"
    SAAT = "SAAT"
    SET="SET"
    SEMS="SEMS"

class StudentSchema(BaseModel):
    matric_number: str
    name: str
    date_of_birth: date
    age: int
    faculty: Faculty
    cgpa: Optional[float] = None


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    matric_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    age: Optional[int] = None
    faculty: Optional[Faculty] = None
    cgpa: Optional[float] = None
    