from pydantic import Field,validator,BaseModel
import re

class PresentedCourses(BaseModel):
    LID:str=Field(max_length=6)
    CID:str=Field(max_length=5,min_length=5)
