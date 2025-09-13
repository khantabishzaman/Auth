from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated, Union
from jose import JWTError, jwt

from . import crud, models, schemas, security
from .database import get_db

app = FastAPI(title="SIH Mentor/Admin Dashboard API")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
    user = crud.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

@app.post("/token", response_model=schemas.Token, tags=["Authentication"])
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=form_data.username)
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = security.create_access_token(
        data={"sub": user.email, "role": str(user.role.value)}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/dashboard", response_model=Union[schemas.AdminDashboard, schemas.MentorDashboard], tags=["Dashboard"])
def get_dashboard_details(current_user: Annotated[models.Employee, Depends(get_current_user)], db: Session = Depends(get_db)):
    if current_user.role == models.UserRole.admin:
        total_students = crud.get_total_student_count(db)
        total_mentors = crud.get_total_mentor_count(db)
        return schemas.AdminDashboard(
            full_name=current_user.full_name, employee_id=current_user.employee_id,
            contact_details=current_user.email, department=current_user.department,
            total_students=total_students, total_mentors=total_mentors
        )
    
    elif current_user.role == models.UserRole.mentor:
        students_assigned = crud.get_students_assigned_to_mentor_count(db, mentor_id=current_user.employee_id)
        sections_taught = crud.get_sections_taught_by_mentor(db, mentor=current_user)
        return schemas.MentorDashboard(
            full_name=current_user.full_name, employee_id=current_user.employee_id,
            contact_details=current_user.email, department=current_user.department,
            total_students_assigned=students_assigned, sections_taught=sections_taught
        )
    
    raise HTTPException(status_code=403, detail="User role not recognized.")
