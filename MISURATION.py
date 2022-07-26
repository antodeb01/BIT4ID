from json import JSONEncoder
from collections import namedtuple
import DB as db

class Misuration:
    def __init__(self,CO2,Temperature,Humidity):
        self.CO2 , self.Temperature , self.Humidity=CO2 , Temperature, Humidity
        
        db.insert_intodb(1,self.CO2,self.Temperature,self.Humidity)
def MisurationDecoder(MisurationDict):
    return  Misuration(*MisurationDict.values())

#M1=Misuration(20,25,12)
db.DB_query()
