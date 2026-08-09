from fastapi import FastAPI,Depends,HTTPException
from database import engine , sessionlocal
import model,validator
from sqlalchemy.orm import Session
import time
app=FastAPI()

while True:
    try:
        model.base.metadata.create_all(bind=engine)
        break
    except:
        print("Database is not ready. Retrying in 2 seconds...")
        time.sleep(2)
def get_db():
    try:
        db=sessionlocal()
        yield db
    finally:
        db.close()

@app.get("/student")
def read_student(db:Session=Depends(get_db)):
    return db.query(model.Student).limit(4).all()


@app.post("/student")
def creat_student(student:validator.student,db:Session=Depends(get_db)):
    student_class=model.Student()
    student_class.STID=student.STID
    student_class.Fname=student.Fname
    student_class.lname=student.lname
    student_class.father=student.father
    student_class.birth=student.birth
    student_class.IDS_number=student.IDS_number
    student_class.borncity=student.borncity
    student_class.address=student.address
    student_class.postalcode=student.postalcode
    student_class.cphone=student.cphone
    student_class.hphone=student.hphone
    student_class.department=student.department
    student_class.major=student.major
    student_class.married=student.married
    student_class.id=student.id
    student_class.SCourseIDs=student.SCourseIDs
    student_class.LIDs=student.LIDs
    student_class.IDS_letter=student.IDS_letter
    student_class.IDS_code=student.IDS_code
    db.add(student_class)
    db.commit()



@app.put("/student/{student_id}")
def update_student(student_id:str,student:validator.student,db:Session=Depends(get_db)):
    student_class=db.query(model.Student).filter(model.Student.STID==student_id).first()
    if student_class is None:
        print("the student is not exsist")
    student_class.STID=student.STID    
    student_class.Fname=student.Fname
    student_class.lname=student.lname
    student_class.father=student.father
    student_class.birth=student.birth
    student_class.IDS_number=student.IDS_number
    student_class.borncity=student.borncity
    student_class.address=student.address
    student_class.postalcode=student.postalcode
    student_class.cphone=student.cphone
    student_class.hphone=student.hphone
    student_class.department=student.department
    student_class.major=student.major
    student_class.married=student.married
    student_class.id=student.id
    student_class.SCourseIDs=student.SCourseIDs
    student_class.LIDs=student.LIDs
    student_class.IDS_letter=student.IDS_letter
    student_class.IDS_code=student.IDS_code
    db.add(student_class)
    db.commit() 
    return student
@app.delete("/student/{student_id}")
def delete_student(student_id:str,db:Session=Depends(get_db)):
    student_class=db.query(model.Student).filter(model.Student.STID==student_id).first()
    if student_class is not None:
        db.query(model.Student).filter(model.Student.STID==student_id).delete()
        db.commit()
        return("دانشجو با موفقیت حذف شد")

@app.get("/teacher")
def read_Teacher(db:Session=Depends(get_db)):
    return db.query(model.Teacher).limit(4).all()

@app.post("/teacher")
def creat_Teacher(teacher:validator.teacher,db:Session=Depends(get_db)):
    Teacher_class=model.Teacher()
    Teacher_class.LID=teacher.LID
    Teacher_class.FName=teacher.FName
    Teacher_class.LName=teacher.LName
    Teacher_class.ID=teacher.ID
    Teacher_class.Department=teacher.Department
    Teacher_class.Major=teacher.Major
    Teacher_class.Birth=teacher.Birth
    Teacher_class.BornCity=teacher.BornCity
    Teacher_class.Address=teacher.Address
    Teacher_class.PostalCode=teacher.PostalCode
    Teacher_class.CPhone=teacher.CPhone
    Teacher_class.HPhone=teacher.HPhone
    Teacher_class.LCourseIDs=teacher.LCourseIDs
    db.add(Teacher_class)
    db.commit()

@app.put("/teacher/{Teacher_id}")
def teacher_update(Teacher_id:str,teacher:validator.teacher,db:Session=Depends(get_db)):
    Teacher_class=db.query(model.Teacher).filter(model.Teacher.LID==Teacher_id).first()
    if Teacher_class is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    Teacher_class.FName=teacher.FName
    Teacher_class.LName=teacher.LName
    Teacher_class.ID=teacher.ID
    Teacher_class.Department=teacher.Department
    Teacher_class.Major=teacher.Major
    Teacher_class.Birth=teacher.Birth
    Teacher_class.BornCity=teacher.BornCity
    Teacher_class.Address=teacher.Address
    Teacher_class.PostalCode=teacher.PostalCode
    Teacher_class.CPhone=teacher.CPhone
    Teacher_class.HPhone=teacher.HPhone
    Teacher_class.LCourseIDs=teacher.LCourseIDs
    db.add(Teacher_class)
    db.commit()
    return teacher

@app.delete("/teacher/{Teacher_id}")
def delete_teacher(Teacher_id:str,db:Session=Depends(get_db)):
    teacher_class=db.query(model.Teacher).filter(model.Teacher.LID==Teacher_id).first()
    if teacher_class is not None:
        db.query(model.Teacher).filter(model.Teacher.LID==Teacher_id).delete()
        db.commit()

@app.get("/Lesson")
def read_Lesson(db:Session=Depends(get_db)):
    return db.query(model.Lesson).limit(4).all()

@app.post("/Lesson")
def creat_Lesson(Lesson:validator.Lesson,db:Session=Depends(get_db)):
    lesson_class=model.Lesson()
    lesson_class.CID=Lesson.CID
    lesson_class.CName=Lesson.CName
    lesson_class.Department=Lesson.Department
    lesson_class.credit=Lesson.credit
    db.add(lesson_class)
    db.commit()

@app.put("/Lesson/{Lesson_id}")
def lesson_update(Lesson:validator.Lesson, lesson_id : str , db:Session=Depends(get_db)):
    lesson_class=db.query(model.Lesson).filter(model.Lesson.CID==lesson_id).first()
    if lesson_class is None:
        print("the Lesson is not exsist")
    lesson_class.CName=Lesson.CName
    lesson_class.Department=Lesson.Department
    lesson_class.credit=Lesson.credit
    db.add(lesson_class)
    db.commit()
    return Lesson

@app.delete("/Lesson/{Lesson_id}")
def lesson_delete(Lesson_id:str,db:Session=Depends(get_db)):
    lesson_class=db.query(model.Lesson).filter(model.Lesson.CID==Lesson_id).first()
    if lesson_class is not None:
        db.query(model.Lesson).filter(model.Lesson.CID==Lesson_id).delete()
        db.commit()

@app.get("/CourseRegister")
def read_CourseRegister(db:Session=Depends(get_db)):
    return db.query(model.CourseRegister).all()
@app.post("/CourseRegister")
def create_course_register(data: validator.CourseRegister,db: Session = Depends(get_db)):
    student = db.query(model.Student).filter(model.Student.STID == data.STID).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    lesson = db.query(model.Lesson).filter(model.Lesson.CID == data.CID).first()
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    course = model.CourseRegister()

    course.STID = student.STID
    course.FName = student.Fname
    course.LName = student.lname

    course.CID = lesson.CID
    course.CName = lesson.CName
    course.Department =lesson.Department
    course.Credit =lesson.Credit

    db.add(course)
    db.commit()

    return course

@app.delete("/CourseRegister/{SID}/{CID}")
def delete_course_register(SID: str,CID: str,db: Session = Depends(get_db)):

    course = db.query(model.CourseRegister).filter(model.CourseRegister.STID == SID,model.CourseRegister.CID == CID).first()

    if course is None:
        raise HTTPException(status_code=404,detail="CourseRegister not found")

    db.delete(course)
    db.commit()

    return {"message": "Course deleted successfully"}

@app.get("/PresentedCourses")
def read_presented_courses(db: Session = Depends(get_db)):
    return db.query(model.PresentedCourses).all()
        

@app.post("/PresentedCourses")
def create_presented_course(data: validator.PresentedCourses,db: Session = Depends(get_db)):
    lesson = db.query(model.Lesson).filter(model.Lesson.CID == data.CID).first()

    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")

    teacher = db.query(model.Teacher).filter(model.Teacher.LID == data.LID).first()

    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")

    present = model.PresentedCourses()

    present.CID = lesson.CID
    present.CName = lesson.CName
    present.Department = lesson.Department
    present.Credit = lesson.credit

    present.LID = teacher.LID
    present.FName = teacher.FName
    present.LName = teacher.LName

    db.add(present)
    db.commit()
    db.refresh(present)

    return present


@app.put("/PresentedCourses/{LID}/{CID}")
def update_presented_course(LID: str,CID: str,data: validator.PresentedCourses,db: Session = Depends(get_db)):

    present = db.query(model.PresentedCourses).filter(model.PresentedCourses.LID == LID,model.PresentedCourses.CID == CID).first()

    if present is None:
        raise HTTPException(status_code=404, detail="Presented course not found")

    lesson = db.query(model.Lesson).filter(model.Lesson.CID == data.CID).first()

    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")

    teacher = db.query(model.Teacher).filter(model.Teacher.LID == data.LID).first()

    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")

    present.CID = lesson.CID
    present.CName = lesson.CName
    present.Department = lesson.Department
    present.Credit = lesson.credit

    present.LID = teacher.LID
    present.FName = teacher.FName
    present.LName = teacher.LName

    db.commit()
    db.refresh(present)

    return present
        

@app.delete("/PresentedCourses/{LID}/{CID}")
def delete_presented_course(LID: str,CID: str,db: Session = Depends(get_db)):

    present = db.query(model.PresentedCourses).filter(model.PresentedCourses.LID == LID,model.PresentedCourses.CID == CID).first()

    if present is None:
        raise HTTPException(status_code=404, detail="Presented course not found")

    db.delete(present)
    db.commit()

    return {"message": "Presented course deleted successfully"}        