#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 16:48:45 2024

@author: caston
"""

# import paho.mqtt.client as mqtt

# def on_connect(client, userdata, flags, rc):
#     print('Connected with result code ' + str(rc))
#     client.subscribe('battery/#')
    
# def on_message(client, userdata, msg):
#     print(msg.topic + "\t" + str(msg.payload))
    
# client = mqtt.Client()

# client.on_connect = on_connect
# client.on_message = on_message

# client.connect('127.0.0.1', 1883, 60)
# client.publish('emqtt', payload='Hello World', qos=0)

# client.loop_forever()

import random
import time
from paho.mqtt import client as mqtt_client

broker = '127.0.0.1'
port = 1883
topic = '/python/mqtt'
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(cleint, userdata, falgs, rc):
        if rc == 0:
            print('Connected to MQTT Broker!')
        else:
            print('Failed to connect, return code %d\n', rc)
    
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    
    return client

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f'message: {msg_count}'
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f'Send `{msg}` to topic `{topic}`')
        else:
            print(f'Failed to send message to topic {topic}')
        msg_count += 1
        
        
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

        
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    
if __name__ == '__main__':
    run()
