from pydantic import Field,validator,BaseModel
import re






class Lesson(BaseModel):
    CID:str=Field(max_length=5,min_length=5)
    CName:str=Field(max_length=25)
    Department:str
    credit:int=Field(ge=1,le=4)
    @validator("CID",pre=True)
    def validata_CID(cls,v):
        if not isinstance(v,str) or not(v.isdigit() and len(v)==5):
            raise ValueError("کد درس باید 5 رقم باشد")
        return v
    @validator("CName",pre=True)
    def validata_CName(cls,v):
        if not isinstance(v,str) or not re.match(r'^[\u0600-\u06FF\s]+$', v):
            raise ValueError("نام درس باید به زبان فارسی باشد")
        return v
    @validator("Department",pre=True)
    def validata_Department(cls,v):
        Departmentes=["اقتصاد","علوم پایه","فنی و مهندسی"]
        if not isinstance(v,str) or v not in Departmentes:
            raise ValueError("دانشکده باید یکی از دانشکده های مجاز باشد ")
        return v
    @validator("credit",pre=True)
    def validata_Credit(cls,v):
        if not isinstance(v,int):
            raise ValueError("تعداد واحد باید عدد باشد")
        return v
    class Config:
        validate_assignment = True
        extra = "forbid"
        strict = True