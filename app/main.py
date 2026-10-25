from fastapi import FastAPI
from app.database import engine , base
from app import model
from app.routers import (student_router,teacher_router,lesson_router,PresentedCourses_router,CourseRegister_router)
import time
from sqlalchemy.exc import OperationalError
app=FastAPI()

while True:
    try:
        base.metadata.create_all(bind=engine)
        break
    except OperationalError:
        print("Database is not ready. Retrying in 2 seconds...")
        time.sleep(2)

app.include_router(student_router.router)
app.include_router(teacher_router.router)
app.include_router(lesson_router.router)
app.include_router(CourseRegister_router.router)
app.include_router(PresentedCourses_router.router)