from sqlalchemy import Column, Integer , String , CheckConstraint,ForeignKey
from sqlalchemy.orm import relationship
from app.database import base
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
        )
    courses = relationship("CourseRegister",back_populates="student")