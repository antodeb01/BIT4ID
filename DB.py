from sqlalchemy import Column, ForeignKey, Integer, String ,Float,Date,Time,Sequence
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import insert
from sqlalchemy import select
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from os import getenv
import time
import datetime


load_dotenv()
engine= create_engine(f'postgresql://{getenv("DB_USER")}:{getenv("DB_PASSWORD")}@{getenv("DB_HOST")}:{getenv("DB_PORT")}/{getenv("DB_NAME")}')
Base=declarative_base()
USER_ID_SEQ = Sequence('user_id_seq')
class Misuration(Base):
    __tablename__ = 'Misuration'
    id=Column(Integer,USER_ID_SEQ,primary_key=True,server_default=USER_ID_SEQ.next_value())
    Date= Column(Date)
    Time=Column(Time)
    CO2=Column(Float)
    Temperature = Column(Integer)
    Humidity = Column(Float)



def db_connect():
    

    Base.metadata.create_all(engine)
    print("Table created succesfully")
    session=Session(engine)
    mis=Misuration(Date=str(datetime.datetime.now()),Time=str(datetime.datetime.now().time()),CO2=0.0,Temperature=0.0,Humidity=0.0)
    print("Misuration object created")
    session.add(mis)
    print("Misuration added succesfully")
    session.commit()
    print("Try table added succesfully ")
    session.delete(mis)
    session.commit()
        
    

            
        
            