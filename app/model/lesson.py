from sqlalchemy import Column, Integer , String , CheckConstraint,ForeignKey
from sqlalchemy.orm import relationship
from app.database import base

    


class Lesson(base):
    __tablename__="Lesson"
    CID=Column(String(5),primary_key=True,index=True)
    CName=Column(String(25),nullable=False)
    Department=Column(String)
    credit=Column(Integer,nullable=False)
    __table_args__=(
        CheckConstraint("credit BETWEEN 1 and 4", name="ck_credit"),
        CheckConstraint('length("CID")=5',name="ck_CID_lesson")
        )
    course_registers = relationship("CourseRegister",back_populates="lesson")
    presented_courses = relationship("PresentedCourses",back_populates="lesson")