from sqlalchemy import Column, Integer , String , CheckConstraint,ForeignKey
from sqlalchemy.orm import relationship
from database import base
class Student(base):
    __tablename__="student"
    STID=Column(String(11),primary_key=True,index=True)
    Fname=Column(String(10),nullable=False)
    lname=Column(String(10),nullable=False)
    father=Column(String(10),nullable=False)
    birth=Column(String)
    IDS_number=Column(String)
    IDS_letter=Column(String)
    IDS_code=Column(String)
    borncity=Column(String)
    address=Column(String(100),nullable=False)
    postalcode=Column(String(10),nullable=False)
    cphone=Column(String(11))
    hphone=Column(String(11))
    department=Column(String)
    major=Column(String)
    married=Column(String)
    id=Column(String(10))
    SCourseIDs=Column(String)
    LIDs=Column(String)
    __table_args__=(
        CheckConstraint('length("STID")=11', name="ck_STID_length"),
        CheckConstraint('length("id") = 10', name="ck_id_length"),
        CheckConstraint('length("postalcode") = 10', name="ck_postal"),
        CheckConstraint("married IN ('مجرد','متاهل')",name="ck_married"),
        CheckConstraint('length("STID")=11',name="ck_STID")
        )
    courses = relationship("CourseRegister",back_populates="student")
    
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
