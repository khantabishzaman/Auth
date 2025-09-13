from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[EmailStr] = None

class AdminDashboard(BaseModel):
    full_name: str
    employee_id: str
    contact_details: EmailStr
    department: Optional[str] = None
    total_students: int
    total_mentors: int
    class Config:
        orm_mode = True

class MentorDashboard(BaseModel):
    full_name: str
    employee_id: str
    contact_details: EmailStr
    department: Optional[str] = None
    total_students_assigned: int
    sections_taught: List[str]
    class Config:
        orm_mode = True
