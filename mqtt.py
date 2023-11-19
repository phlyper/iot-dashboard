from faker import Faker
import paho.mqtt.client as paho
import time
from paho import mqtt
import datetime
import json

from config import load_config
config = load_config()

fake = Faker(['fr_FR', 'en_US'])

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print('CONNACK received with code %s.' % (rc))
    
# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))  

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(config['MQTT_USERNAME'], config['MQTT_PASSWORD'])
client.connect(config['MQTT_HOST'], config['MQTT_PORT'])
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("encyclopedia/#", qos=1)

# a single publish, this can also be done in loops, etc.
client.publish("encyclopedia/temperature", payload="hot", qos=1)

client.loop_start()

i = 0
while  i< 10:
    # a single publish, this can also be done in loops, etc.
    client.publish("encyclopedia/temperature", payload="hot %s %s" % (fake.unique.random_int(min=0, max=40), time.time()), qos=1)
    i += 1
    time.sleep(5)

client.loop_forever()
