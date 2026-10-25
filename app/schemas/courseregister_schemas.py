from pydantic import Field,validator,BaseModel
import re


class CourseRegister(BaseModel):
    CID:str=Field(max_length=5,min_length=5)
    STID:str=Field(min_length=11,max_length=11)