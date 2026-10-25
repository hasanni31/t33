from pydantic import Field,validator,BaseModel
import re





class teacher(BaseModel):
    LID:str=Field(max_length=6)
    FName:str=Field(max_length=10)
    LName:str=Field(max_length=10)
    ID:str=Field(max_length=10 , min_length=10)
    Department:str
    Major:str
    Birth:str
    BornCity:str
    Address:str=Field(max_length=100)
    PostalCode:str=Field(max_length=10 , min_length=10)
    CPhone:str=Field(max_length=11 , min_length=11)
    HPhone:str=Field(max_length=11 , min_length=11)
    LCourseIDs:str
    @validator("LID",pre=True)
    def validata_LID(cls,v):
        if not isinstance(v,str) or not(v.isdigit() and len(v)==6):
            raise ValueError("کد استاد باید یک عدد 6 رقمی باشد")
        return v
    @validator("FName",pre=True)
    def validata_FName_teacher(cls,v):
        if not isinstance(v,str) or not re.match(r'^[\u0600-\u06FF\s]+$',v):
            raise ValueError("نام باید فارسی باشد و 10 کاراکتر")
        return v
    @validator("LName",pre=True)
    def validata_LName_teacvher(cls,v):
        if not isinstance(v,str) or not re.match(r'^[\u0600-\u06FF\s]+$',v):
            raise ValueError("نام خانوادگی باید فارسی و 10 کاراکتر باشد")
        return v
    @validator("ID",pre=True)
    def validata_ID(cls,v):
        if not isinstance(v,str) or not(v.isdigit() and len(v)==10):
            raise ValueError("کد ملی باید عددی 10 رقمی باشد")
        return v
    @validator("Department",pre=True)
    def validata_Department(cls,v):
        Departmentes=["اقتصاد","علوم پایه","فنی و مهندسی"]
        if not isinstance(v,str) or v not in Departmentes:
            raise ValueError("دانشکده باید یکی از دانشکده های مجاز باشد")
        return v
    @validator("Major",pre=True)
    def validata_Major(cls,v):
        Majors={
            "فنی و مهندسی": [
                "مهندسی کامپیوتر", "مهندسی برق", "مهندسی مکانیک", "مهندسی عمران",
                "مهندسی صنایع", "مهندسی شیمی", "مهندسی مواد", "مهندسی هوافضا",
                "مهندسی نفت", "مهندسی معماری"
            ],
            "علوم پایه": [
                "ریاضی", "فیزیک", "شیمی", "زیست‌شناسی", "زمین‌شناسی",
                "آمار", "علوم کامپیوتر", "بیوشیمی", "میکروبیولوژی", "ژنتیک"
            ],
            "اقتصاد": [
                "اقتصاد", "مدیریت بازرگانی", "حسابداری", "مدیریت مالی",
                "مدیریت صنعتی", "اقتصاد کشاورزی", "اقتصاد بین‌الملل",
                "بانکداری", "بیمه", "مدیریت دولتی"
            ]
        }
        if not isinstance(v,str):
            raise ValueError("رشته باید به صورت رشته باشد")
        for dept, Major_list in Majors.items():
            if v in Major_list:
                return v
        raise ValueError("رشته تحصیلی باید مرتبط بارشته دانشکده باشد")
    @validator("Birth",pre=True)
    def validata_Birth(cls,v):
        if not isinstance(v,str):
            raise ValueError("تاریخ باید به صورت رشته باشد")
        try:
            year,month,day=map(int,v.split("/"))
            if not(1300 <= year <= 1400 and 1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError("سال باید بین ۱۳۰۰ تا ۱۴۰۰، ماه بین ۱ تا ۱۲ و روز بین ۱ تا ۳۱ باشد")
        except:
            raise ValueError("فرمت تاریخ باید به صورت شمسی YYYY/MM/DD باشد")
        return v
    @validator("BornCity",pre=True)
    def validata_BornCity(cls,v):
        BornCitys=[
            "تهران", "مشهد", "اصفهان", "کرج", "شیراز", "تبریز", "قم", "اهواز", "کرمانشاه",
            "ارومیه", "رشت", "زاهدان", "همدان", "کرمان", "یزد", "اردبیل", "بندرعباس",
            "اراک", "اسلامشهر", "زنجان", "سنندج", "قزوین", "خرم‌آباد", "گرگان",
            "ساری", "بجنورد", "بوشهر", "بیرجند", "ایلام", "شهرکرد", "یاسوج"
            ]
        if not isinstance(v,str) or v not in BornCitys:
            raise ValueError("محل تولد باید یکی از مراکز استان کشور باشد")
        return v
    @validator("Address",pre=True)
    def validata_Address(cls,v):
        if not isinstance(v,str) or not len(v)<=100:
            raise ValueError("ادرس باید یک رشته با حداکثر 100 کاراکتر باشد")
        return v
    @validator("PostalCode",pre=True)
    def validata_PostalCode(cls,v):
        if not isinstance(v,str) or not(v.isdigit()  and len(v)==10):
            raise ValueError("کد پستی باید عددی 10 رقمی باشد")
        return v
    @validator("CPhone",pre=True)
    def validata_CPhone(cls,v):
        if not isinstance(v,str) or not re.match(r'^0\d{2,3}\d{8}$', v):
            raise ValueError("شماره تلفن باید 11 رقم باشد")
        return v
    @validator("HPhone",pre=True)
    def validata_HPhone(cls,v):
        if not isinstance(v,str) or not re.match(r'^0\d{2,3}\d{8}$', v):
            raise ValueError("شماره تلفن ثابت باید بر اسا کد استان باشد مثل(06633462312)")
        return v
    @validator("LCourseIDs",pre=True)
    def validata_LCourseIDs(cls,v):
        if not isinstance(v,str) or not(v.isdigit() and len(v)==5):
            raise ValueError("کد درس باید عدد 5 رقمی باشد")
        return v
    class Config:
        validate_assignment = True
        extra = "forbid"
        strict = True