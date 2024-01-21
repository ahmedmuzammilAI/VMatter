import paho.mqtt.client as paho             #mqtt library
import time
from datetime import datetime
import random

ACCESS_TOKEN='brxtwYmvXh2QgbJfqzvK'                 #Token of your device
broker="demo.thingsboard.io"                        #host name
port=1883                                           #data listening port

def on_publish(client,userdata,result):             #create function for callback
    print("data published to thingsboard \n")
    pass

client1= paho.Client("control1")                    #create client object
client1.on_publish = on_publish                     #assign function to callback
client1.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device
client1.connect(broker,port,keepalive=60)           #establish connection

def generate_blood_pressure():
    systolic = round(random.uniform(100, 160))  # Adjust range as needed
    diastolic = round(random.uniform(60, 90))  # Adjust range as needed
    # bp= str(systolic)+str(diastolic)
    return systolic, diastolic

def generate_heart_rate():
    heart_rate = random.uniform(60, 100)  # Adjust range as needed
    return heart_rate

def generate_temperature():
    temperature = random.uniform(35.5, 37.5)  # Adjust range as needed
    return temperature

def generate_spo2():
    spo2 = random.uniform(95, 100)  # Adjust range as needed
    return spo2

def generate_payload(systolic, diastolic, heart_rate, body_temp, spo2):
    """Generates a JSON payload with health readings, allowing individual updates."""
    payload = {
        "systolic": systolic,
        "diastolic": diastolic,
        "heart_rate": heart_rate,
        "body_temp": body_temp,
        "spo2": spo2
    }
    return (payload)

while True:

    systolic,diastolic = generate_blood_pressure()
    systolic=round(systolic)
    diastolic=round(diastolic)
    heart_rate = round(generate_heart_rate())
    body_temp = round(generate_temperature(),2)
    spo2 = round(generate_spo2(),1)
    payload = generate_payload(systolic, diastolic, heart_rate, body_temp, spo2)
    payload["heart_rate"]=30

    ret= client1.publish("v1/devices/me/telemetry",str(payload)) #topic-v1/devices/me/telemetry
    print("Please check LATEST TELEMETRY field of your device")
    print(payload)
    time.sleep(1)

