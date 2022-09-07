# python 3.6

import random
import time
import json
from paho.mqtt import client as mqtt_client
import datetime

broker = '127.0.0.1'
port = 1883
topic = "sensors/data"



def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client()
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client



def publish(client):
    msg_count = 0
    while True:
        time.sleep(5)
        msg = f'{"{"}"CO2":{round(random.gauss(20,8),2)},"Temperature":{round(random.gauss(20,10),2)},"Humidity":{round(random.gauss(30,12),2)}{"}"}'
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
