from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from datetime import date
from typing import Optional
from sqlalchemy import Date, Float, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# 1. Your database URL
DATABASE_URL = "postgresql+psycopg://postgres:password@localhost:5432/student_management"


# 2. Engine (connection to Postgres)
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True)


# 3. Session factory (this creates DB sessions)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)


# 4. Base class for all models
class Base(DeclarativeBase):
    pass


# 2. This is your SQLAlchemy Model
class Student(Base):
    __tablename__ = "students"  # This tells Postgres what to name the table
    
    # These define the columns using SQLAlchemy types
    matric_number: Mapped[str] = mapped_column(String(20), primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    age: Mapped[int] = mapped_column(Integer)
    cgpa: Mapped[Optional[float]] = mapped_column(Float)
    faculty: Mapped[str] = mapped_column(String(50))
    date_of_birth: Mapped[date] = mapped_column(Date)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()