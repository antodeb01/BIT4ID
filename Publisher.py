# python 3.6

import random
import time
import json
from paho.mqtt import client as mqtt_client


broker = '127.0.0.1'
port = 1883
topic = "sensors/data"
client_id = 'emqx_2203261'
username = 'admin'
password = 'public'


def connect_mqtt():
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


def publish(client):
    
    while True:
        time.sleep(5)
        with open('Misuration.json','r') as json_file:
            jsonMeasure= json.load(json_file)
            Measure=json.JSONEncoder().encode(jsonMeasure)      
        result = client.publish(topic, Measure)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{Measure}` to topic .`{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
      


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
