from sqlalchemy.orm import Session
from . import models

def get_user_by_email(db: Session, email: str):
    return db.query(models.Employee).filter(models.Employee.email == email).first()

def get_total_student_count(db: Session) -> int:
    return db.query(models.Student).count()

def get_total_mentor_count(db: Session) -> int:
    return db.query(models.Employee).filter(models.Employee.role == 'mentor').count()

def get_students_assigned_to_mentor_count(db: Session, mentor_id: str) -> int:
    return db.query(models.Student).filter(models.Student.mentor_id == mentor_id).count()

def get_sections_taught_by_mentor(db: Session, mentor: models.Employee) -> list[str]:
    sections = mentor.sections
    return [f"{section.course_name} ({section.course_code})" for section in sections]
