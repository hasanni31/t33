from fastapi import APIRouter,Depends,HTTPException
from app import model
from app.schemas import teacher_schemas
from app.deps import get_db
from sqlalchemy.orm import Session

router=APIRouter(prefix="/Teacher",tags=["Teacher"])


@router.get("/")
def read_Teacher(db:Session=Depends(get_db)):
    return db.query(model.Teacher).limit(4).all()

@router.post("/")
def creat_Teacher(data:teacher_schemas.teacher,db:Session=Depends(get_db)):
    exists=db.query(model.Teacher).filter(model.Teacher.LID==data.LID).first()
    if exists is not None:
        raise HTTPException(status_code=409, detail="teacher already exists")
    Teacher_class=model.Teacher(**data.model_dump())
    db.add(Teacher_class)
    db.commit()
    return Teacher_class

@router.put("/{Teacher_id}")
def teacher_update(Teacher_id:str,data:teacher_schemas.teacher,db:Session=Depends(get_db)):
    Teacher_class=db.query(model.Teacher).filter(model.Teacher.LID==Teacher_id).first()
    if Teacher_class is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    for key , value in data.model_dump(exclude={"LID"}).items():
        setattr(Teacher_class,key,value)
    db.add(Teacher_class)
    db.commit()
    return data

@router.delete("/{Teacher_id}")
def delete_teacher(Teacher_id:str,db:Session=Depends(get_db)):
    teacher_class=db.query(model.Teacher).filter(model.Teacher.LID==Teacher_id).first()
    if teacher_class is None:
        raise HTTPException(status_code=404,detail="teacher not found")
    db.delete(teacher_class)
    db.commit()
    return(".استاد با موفقیت حذف شد")