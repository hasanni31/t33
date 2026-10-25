from sqlalchemy import Column, Integer , String , CheckConstraint,ForeignKey
from sqlalchemy.orm import relationship
from app.database import base

    
class CourseRegister(base):
    __tablename__="CourseRegister"
    CID=Column(String(5),ForeignKey("Lesson.CID"),primary_key=True,index=True)
    CName=Column(String)
    Department=Column(String)
    Credit=Column(Integer)
    STID=Column(String(11),ForeignKey("student.STID"),primary_key=True,index=True)
    Fname=Column(String)
    lname=Column(String)
    student = relationship("Student",back_populates="courses")
    lesson = relationship("Lesson",back_populates="course_registers")