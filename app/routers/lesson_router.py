from fastapi import APIRouter,Depends,HTTPException
from app import model  
from app.schemas import Lesson_schemas
from app.deps import get_db
from sqlalchemy.orm import Session

router=APIRouter(prefix="/Lesson",tags=["Lesson"])


@router.get("/")
def read_Lesson(db:Session=Depends(get_db)):
    return db.query(model.Lesson).limit(4).all()

@router.post("/")
def creat_Lesson(data:Lesson_schemas.Lesson,db:Session=Depends(get_db)):
    exists=db.query(model.Lesson).filter(model.Lesson.CID==data.CID).first()
    if exists is not None:
        raise HTTPException(status_code=409, detail="Lesson already exists")
    lesson_class=model.Lesson()
    lesson_class.CID=data.CID
    lesson_class.CName=data.CName
    lesson_class.Department=data.Department
    lesson_class.credit=data.credit
    db.add(lesson_class)
    db.commit()
    return lesson_class

@router.put("/{lesson_id}")
def lesson_update(data:Lesson_schemas.Lesson, lesson_id : str , db:Session=Depends(get_db)):
    lesson_class=db.query(model.Lesson).filter(model.Lesson.CID==lesson_id).first()
    if lesson_class is None:
        raise HTTPException(status_code=404, detail="lesson not found")
    lesson_class.CName=data.CName
    lesson_class.Department=data.Department
    lesson_class.credit=data.credit
    db.add(lesson_class)
    db.commit()
    return data

@router.delete("/{lesson_id}")
def lesson_delete(lesson_id:str,db:Session=Depends(get_db)):
    lesson_class=db.query(model.Lesson).filter(model.Lesson.CID==lesson_id).first()
    if lesson_class is  None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    db.delete(lesson_class)
    db.commit()
    return {"message": "Lesson deleted successfully"}