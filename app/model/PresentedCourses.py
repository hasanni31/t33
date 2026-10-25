from sqlalchemy import Column, Integer , String , CheckConstraint,ForeignKey
from sqlalchemy.orm import relationship
from app.database import base


class PresentedCourses(base):
    __tablename__="PresentedCourses"
    CID=Column(String(5),ForeignKey("Lesson.CID"),primary_key=True,index=True)
    CName=Column(String)
    Department=Column(String)
    Credit=Column(Integer)
    LID=Column(String(6),ForeignKey("teacher.LID"),primary_key=True,index=True)
    Fname=Column(String)
    lname=Column(String)
    lesson = relationship("Lesson",back_populates="presented_courses")
    teacher = relationship("Teacher",back_populates="presented_courses")   
