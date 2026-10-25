from app.database import sessionlocal

def get_db():
    try:
        db=sessionlocal()
        yield db
    finally:
        db.close()