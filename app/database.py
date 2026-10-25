from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
sqlalchemy_database_url= "postgresql+psycopg2://postgres:406153@db:5432/university"

engine=create_engine(sqlalchemy_database_url)
sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
base=declarative_base()
 