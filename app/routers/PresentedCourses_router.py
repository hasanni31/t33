from fastapi import APIRouter,Depends,HTTPException
from app import model 
from app.schemas import presentedcourses_schemas
from app.deps import get_db
from sqlalchemy.orm import Session

router=APIRouter(prefix="/PresentedCourses",tags=["PresentedCourses"])


@router.get("/")
def read_presented_courses(db: Session = Depends(get_db)):
    return db.query(model.PresentedCourses).all()
        

@router.post("/")
def create_presented_course(data: presentedcourses_schemas.PresentedCourses,db: Session = Depends(get_db)):
    lesson = db.query(model.Lesson).filter(model.Lesson.CID == data.CID).first()

    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")

    teacher = db.query(model.Teacher).filter(model.Teacher.LID == data.LID).first()

    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    exists=db.query(model.PresentedCourses).filter(model.PresentedCourses.CID==data.CID,model.PresentedCourses.LID==data.LID).first()
    if exists is not None:
        raise HTTPException(status_code=409, detail="Presented course already exists")

    present = model.PresentedCourses()

    present.CID = lesson.CID
    present.CName = lesson.CName
    present.Department = lesson.Department
    present.Credit = lesson.credit

    present.LID = teacher.LID
    present.Fname = teacher.FName
    present.lname = teacher.LName

    db.add(present)
    db.commit()
    db.refresh(present)

    return present


@router.put("/{LID}/{CID}")
def update_presented_course(LID: str,CID: str,db: Session = Depends(get_db)):

    present = db.query(model.PresentedCourses).filter(model.PresentedCourses.LID == LID,model.PresentedCourses.CID == CID).first()

    if present is None:
        raise HTTPException(status_code=404, detail="Presented course not found")

    lesson = db.query(model.Lesson).filter(model.Lesson.CID ==CID).first()

    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")

    teacher = db.query(model.Teacher).filter(model.Teacher.LID ==LID).first()

    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")

    
    present.CName = lesson.CName
    present.Department = lesson.Department
    present.Credit = lesson.credit

    
    present.Fname = teacher.FName
    present.lname = teacher.LName

    db.commit()
    db.refresh(present)

    return present
        

@router.delete("/{LID}/{CID}")
def delete_presented_course(LID: str,CID: str,db: Session = Depends(get_db)):

    present = db.query(model.PresentedCourses).filter(model.PresentedCourses.LID == LID,model.PresentedCourses.CID == CID).first()

    if present is None:
        raise HTTPException(status_code=404, detail="Presented course not found")

    db.delete(present)
    db.commit()

    return {"message": "Presented course deleted successfully"}     