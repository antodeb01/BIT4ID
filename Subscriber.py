
# python3.6
import MISURATION as M 
import random
import json
from paho.mqtt import client as mqtt_client

broker = '127.17.0.1'
port = 1883
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
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received {json.loads(msg.payload.decode())}` from `{msg.topic}` topic")
        Payloads.append(msg.payload.decode())
    client.subscribe(topic)
    client.on_message = on_message
def     


def run():
    DB_init()
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
   


if __name__ == '__main__':
    run()




