
import json
import datetime
import DB as db
import dateutil.parser
import re
import random
import json
from paho.mqtt import client as mqtt_client
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from os import getenv
import time


load_dotenv()


broker = getenv("MQTT_BROKER")
port = int(getenv("MQTT_PORT"))
topic = "sensors/data"




def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client() 
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received {msg.payload.decode()}` from `{msg.topic}` topic")
        session=Session(db.engine)
        misuration_SAVER(msg.payload.decode(),session)
    client.subscribe(topic)
    client.on_message=on_message
    

def date_hook(json_dict):
    for (key, value) in json_dict.items():
        if type(value) is str and re.match('^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d*$', value):
            json_dict[key] = dateutile.parser.parse(value)
        elif type(value) is str and re.match('^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', value):
            json_dict[key] = dateutil.parser.parse(value)
        else:
            pass
    return json_dict 


def misuration_SAVER(msg,session):
         
    obj=json.loads(msg)
    misuration = db.Misuration(Date=str(datetime.datetime.now()),Time=str(datetime.datetime.now().time()),CO2=obj.get("CO2"),Temperature=obj.get("Temperature"),Humidity = obj.get("Humidity"))
    
    session.add(misuration)
    session.commit()





def run():
    for i in range(10):
        try:

            db.db_connect()
            break
        except:
            time.sleep(10)
            print(f"{i} try to connect")    
    else:
        raise Exception      
    client = connect_mqtt() #connect to mqtt broker
     
    subscribe(client) #invoke the subscribe method: receive payloads from broker decode and save it in a queue
    
    client.loop_forever()
   


if __name__ == '__main__':
    run()




