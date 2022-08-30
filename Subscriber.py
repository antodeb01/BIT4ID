
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



load_dotenv()


broker = getenv("MQTT_BROKER")
port = int(getenv("MQTT_PORT"))
topic = "sensors/data"
client_id = 'emqx_Njk0MT'
username = 'admin'
password = 'public'
Payloads=[]


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received {json.loads(msg.payload.decode())}` from `{msg.topic}` topic")
        Payloads.append(msg.payload.decode())
    client.subscribe(topic)
    client.on_message = on_message


def date_hook(json_dict):
    for (key, value) in json_dict.items():
        if type(value) is str and re.match('^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d*$', value):
            json_dict[key] = dateutile.parser.parse(value)
        elif type(value) is str and re.match('^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', value):
            json_dict[key] = dateutil.parser.parse(value)
        else:
            pass
    return json_dict 


def misuration_SAVER(lst: list,session):
    while lst:
        jobj=lst[0]
        obj=json.loads(jobj,object_hook=date_hook)
        misuration = db.Misuration(Date=obj.get("datetime"),Time=obj.get("datetime").time(),CO2=obj.get("CO2"),Temperature=obj.get("Temperature"),Humidity = obj.get("Humidity"))
        lst.pop(0)
        session.add(misuration)
        session.commit()




def run():
    session=Session(db.engine) #open a session with db
    client = connect_mqtt() #connect to mqtt broker
    subscribe(client) #invoke the subscribe method: receive payloads from broker decode and save it in a queue
    while True:
        misuration_SAVER(Payloads,session) #extract elements from payloads queue and save it into db
    client.loop_forever()
   


if __name__ == '__main__':
    run()




