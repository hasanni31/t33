from sqlalchemy import Column, Integer , String , CheckConstraint,ForeignKey
from sqlalchemy.orm import relationship
from app.database import base

    
class Teacher(base):
    __tablename__="teacher"
    LID=Column(String(6),primary_key=True,index=True)
    FName=Column(String(10))
    LName=Column(String(10))
    ID=Column(String(10))
    Department=Column(String)
    Major=Column(String)
    Birth=Column(String)
    BornCity=Column(String)
    Address=Column(String(100))
    PostalCode=Column(String(10))
    CPhone=Column(String(11))
    HPhone=Column(String(11))
    LCourseIDs=Column(String)
    __table_args__=(
        CheckConstraint('length("LID")=6',name="ck_lid_teacher"),
        CheckConstraint('length("ID")=10',name="ck_id_teacher")
        )
    presented_courses = relationship("PresentedCourses",back_populates="teacher")