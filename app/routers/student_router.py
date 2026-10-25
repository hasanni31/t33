from fastapi import APIRouter,Depends,HTTPException
from app import model 
from app.schemas import student_schemas
from app.deps import get_db
from sqlalchemy.orm import Session

router=APIRouter(prefix="/student",tags=["student"])


@router.get("/")
def read_student(db:Session=Depends(get_db)):
    return db.query(model.Student).limit(4).all()


@router.post("/")
def creat_student(data:student_schemas.student,db:Session=Depends(get_db)):
    exists=db.query(model.Student).filter(model.Student.STID==data.STID).first()
    if exists is not None:
        raise HTTPException(status_code=409, detail="student already exists")
    student_class = model.Student(**data.model_dump())
    db.add(student_class)
    db.commit()



@router.put("/{student_id}")
def update_student(student_id:str,data:student_schemas.student,db:Session=Depends(get_db)):
    student_class=db.query(model.Student).filter(model.Student.STID==student_id).first()
    if student_class is None:
        raise HTTPException(status_code=404, detail="student not found")   
    for key, value in data.model_dump(exclude={"STID"}).items():
        setattr(student_class, key, value)
    db.add(student_class)
    db.commit() 
    return data
@router.delete("/{student_id}")
def delete_student(student_id:str,db:Session=Depends(get_db)):
    student_class=db.query(model.Student).filter(model.Student.STID==student_id).first()
    if student_class is None:
        raise HTTPException(status_code=404, detail="student not found")
    db.delete(student_class)
    db.commit()
    return("دانشجو با موفقیت حذف شد")