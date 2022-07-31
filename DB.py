from sqlalchemy import Column, ForeignKey, Integer, String ,Float,Date,Time,Sequence
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import insert
from sqlalchemy import select



engine= create_engine('postgresql://postgres:bit4id@localhost:5432/postgres')
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

Base.metadata.create_all(engine)
   