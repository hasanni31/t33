from pydantic import Field,validator,BaseModel
import re








class student(BaseModel):
    STID:str=Field(min_length=11,max_length=11)
    Fname:str=Field(max_length=10)
    lname:str=Field(max_length=10)
    father:str=Field(max_length=10)
    birth:str
    IDS_number:str
    IDS_letter:str
    IDS_code:str
    borncity:str
    address:str=Field(max_length=100)
    postalcode:str=Field(max_length=10,min_length=10)
    cphone:str=Field(max_length=11,min_length=11)
    hphone:str=Field(max_length=11,min_length=11)
    department:str
    major:str
    married:str
    id:str=Field(max_length=10,min_length=10)
    SCourseIDs:str
    LIDs:str
    @validator("STID",pre=True)
    def validate_STID_student(cls,v):
        if not isinstance(v,str) or not(v.isdigit() and len(v)==11):
            raise ValueError("کد دانشجویی باید 11 رقم باشد ")
        if not v[3:9]=="114150":
            raise ValueError("کد دانشگاه باید 114150 باشد")
        return v
    @validator("Fname", pre=True)
    def validate_fname_student(cls,v):
        if not isinstance(v,str) or not re.match(r'^[\u0600-\u06FF\s]+$', v):
            raise ValueError("نام باید حاوی کاراکتر های فارسی باشد ")
        return v
    @validator("lname", pre=True)
    def validate_lname_student(cls,v):
        if not isinstance(v,str) or not re.match(r'^[\u0600-\u06FF\s]+$', v):
             raise ValueError("نام خانوادگی باید حاوی کاراکتر های فارسی باشد ")
        return v
    @validator("father", pre=True)
    def validate_father_names(cls,v):
        if not isinstance(v,str) or not re.match(r'^[\u0600-\u06FF\s]+$', v):
            raise ValueError("نام پدر باید حاوی کاراکتر های فارسی باشد ")
        return v
    @validator("birth",pre=True)
    def  validate_birth_date(cls,v):
        if not isinstance(v,str):
            raise ValueError("تاریخ تولد باید رشته باشد")
        try:
            year, month, day=map(int,v.split("/"))
            if not(1300<=year<=1400 and 1<=month<=12 and 1<=day<=31):
                raise ValueError("سال باید بین ۱۳۰۰ تا ۱۴۰۰، ماه بین ۱ تا ۱۲ و روز بین ۱ تا ۳۱ باشد")
                      
        except:
            raise ValueError("فرمت تاریخ باید به صورت شمسی YYYY/MM/DD باشد")
        return v
    @validator("IDS_number",pre=True)
    def validate_ids_number(cls,v):
        if not isinstance(v,str) or not(v.isdigit() and len(v)==6):
            raise ValueError("سریال شناسنامه باید عددی 6 رقمی باشد")
        return v
    @validator("IDS_letter", pre=True)
    def validata_ids_letter(cls,v):
        persian_letters ="ضصثقفغعهخحجچپگکمنتالبیسشظطزرذدئو"
        if not isinstance(v,str) or not v in persian_letters:
            raise ValueError("حرف سریال شناسنامه باید یکی از حروف الفبای فارسی باشد")
        return v
    @validator("IDS_code",pre=True)
    def validata_ids_code(cls,v):
        if not isinstance(v,str) or not(v.isdigit() and len(v)==2):
            raise ValueError("کد سریال شناسنامه باید عدد 2 رقمی باشد")
        return v 
    @validator("borncity", pre=True)
    def validata_born_city(cls,v):
        cities = [
            "تهران", "مشهد", "اصفهان", "کرج", "شیراز", "تبریز", "قم", "اهواز", "کرمانشاه",
            "ارومیه", "رشت", "زاهدان", "همدان", "کرمان", "یزد", "اردبیل", "بندرعباس",
            "اراک", "اسلامشهر", "زنجان", "سنندج", "قزوین", "خرم‌آباد", "گرگان",
            "ساری", "بجنورد", "بوشهر", "بیرجند", "ایلام", "شهرکرد", "یاسوج"
            ]
        if not isinstance(v,str) or v not in cities:
            raise ValueError("محل  تولد باید یکی از مراکز استان ایران باشد")
        return v
    @validator("address", pre=True)
    def validata_address(cls,v):
        if not isinstance(v,str) or  len(v)>100:
            raise ValueError("ادرس باید حداکثر 100 کاراکتر باشد")
        return v
    @validator("postalcode", pre=True)
    def validata_postal_code(cls,v):
        if not isinstance(v,str) or not(v.isdigit()  and  len(v)==10):
            raise ValueError("کد پستی باید عددی 10 رقمی باشه")
        return v
    @validator("cphone",pre=True)
    def validata_cphone(cls,v):
        if not isinstance(v,str) or not  re.match(r'^0\d{2,3}\d{8}$', v):
            raise ValueError("شماره تلفن باید عددی 11 رقمی باشد")
        return v
    @validator("hphone",pre=True)
    def validata_HPhone(cls,v):
        if not isinstance(v,str) or not re.match(r'^0\d{2,3}\d{8}$', v):
            raise ValueError("تلفن ثابت باید بر اساس کد استان باشد مثل(06633222340)")
        return v
    @validator("department",pre=True)
    def validata_Department(cls,v):
        departmentes=["فنی و مهندسی","علوم پایه","اقتصاد"]
        if not isinstance(v,str) or v not in departmentes:
            raise ValueError("دانشکده باید یکی از دانشکده های مجاز باشد")
        return v
    @validator("major",pre=True)
    def validata_major(cls,v):
        majors={
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
            raise ValueError("رشته تحصیلی باید رشته باشد")
        for dept,major_list in majors.items():
            if v in major_list :
                return v
        raise ValueError("رشته تحصیلی باید یکی از رشته های مرتبط با دانشکده باشد")
    @validator("married",pre=True)
    def validata_Married(cls,v):
        Marrieds="مجرد","متاهل"
        if not isinstance(v,str) or v not in Marrieds:
            raise ValueError("وضعیت تاهل باید مجرد یا متاهل باشد")
        return v
    @validator("id",pre=True)
    def validata_ID(cls,v):
        if not isinstance(v,str) or not(v.isdigit() and len(v)==10):
            raise ValueError("کد ملی باید عدد 10 رقمی باشد")
        return v
    @validator("SCourseIDs",pre=True)
    def validata_SCourseIDs(cls,v):
        if not isinstance(v,str) or not(v.isdigit() and len(v)==5):
            raise ValueError("کد درس باید ععدی 5 رقمی باشد ")
        return v
    @validator("LIDs",pre=True)
    def validata_LIDs(cls,v):
        if not isinstance(v,str) or not(v.isdigit() and len(v)==6):
            raise ValueError("کد اساتید باید عددی 6 رقمی باشد")
        return v
    class Config:
        validate_assignment = True
        extra = "forbid"
        strict = True