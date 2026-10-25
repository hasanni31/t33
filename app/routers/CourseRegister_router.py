from fastapi import APIRouter,Depends,HTTPException
from app import model 
from app.schemas import courseregister_schemas
from app.deps import get_db
from sqlalchemy.orm import Session
router=APIRouter(prefix="/CourseRegister",tags=["CourseRegister"])


@router.get("/")
def read_CourseRegister(db:Session=Depends(get_db)):
    return db.query(model.CourseRegister).all()
@router.post("/")
def create_course_register(data: courseregister_schemas.CourseRegister,db: Session = Depends(get_db)):
    student = db.query(model.Student).filter(model.Student.STID == data.STID).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    lesson = db.query(model.Lesson).filter(model.Lesson.CID == data.CID).first()
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    exsist=db.query(model.CourseRegister).filter(model.CourseRegister.STID==data.STID,model.CourseRegister.CID==data.CID).first()
    if exsist is not None:
        raise HTTPException(status_code=409, detail="Already registered")
    course = model.CourseRegister()

    course.STID = student.STID
    course.FName = student.Fname
    course.lName = student.lname

    course.CID = lesson.CID
    course.CName = lesson.CName
    course.Department =lesson.Department
    course.Credit =lesson.Credit

    db.add(course)
    db.commit()

    return course

@router.delete("/{SID}/{CID}")
def delete_course_register(SID: str,CID: str,db: Session = Depends(get_db)):

    course = db.query(model.CourseRegister).filter(model.CourseRegister.STID == SID,model.CourseRegister.CID == CID).first()

    if course is None:
        raise HTTPException(status_code=404,detail="CourseRegister not found")

    db.delete(course)
    db.commit()

    return {"message": "Course deleted successfully"}