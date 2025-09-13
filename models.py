import enum
from sqlalchemy import (Column, String, DATE, Enum, ForeignKey, Integer, TIMESTAMPTZ)
from sqlalchemy.orm import relationship
from .database import Base

class UserRole(str, enum.Enum):
    admin = "admin"
    mentor = "mentor"

class Employee(Base):
    __tablename__ = "employees"
    employee_id = Column(String(100), primary_key=True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    dob = Column(DATE)
    date_joined = Column(TIMESTAMPTZ)
    department = Column(String(255))
    role = Column(Enum(UserRole), nullable=False)
    students = relationship("Student", back_populates="mentor")
    sections = relationship("Section", secondary="mentor_section_assignments", back_populates="mentors")

class Student(Base):
    __tablename__ = "students"
    student_id = Column(Integer, primary_key=True)
    enrollment_number = Column(String(100), unique=True, nullable=False)
    full_name = Column(String(255), nullable=False)
    mentor_id = Column(String(100), ForeignKey("employees.employee_id"))
    mentor = relationship("Employee", back_populates="students")

class Section(Base):
    __tablename__ = "sections"
    section_id = Column(Integer, primary_key=True)
    course_name = Column(String(255), nullable=False)
    course_code = Column(String(50), nullable=False)
    mentors = relationship("Employee", secondary="mentor_section_assignments", back_populates="sections")

class MentorSectionAssignment(Base):
    __tablename__ = "mentor_section_assignments"
    mentor_id = Column(String(100), ForeignKey("employees.employee_id"), primary_key=True)
    section_id = Column(Integer, ForeignKey("sections.section_id"), primary_key=True)
