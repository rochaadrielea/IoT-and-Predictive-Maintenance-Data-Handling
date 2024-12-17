import paho.mqtt.client as mqtt
import time

broker = "broker.hivemq.com"  # Public MQTT broker
port = 1883

def on_connect(client, userdata, flags, rc):
    print(f"Connection result: {rc}")
    if rc == 0:
        print("Connected successfully!")
    else:
        print("Connection failed!")

client = mqtt.Client()
client.on_connect = on_connect

try:
    print("Attempting to connect to the MQTT broker...")
    client.connect(broker, port, 60)
    client.loop_start()
    time.sleep(5)  # Wait for connection
    client.loop_stop()
    print("Finished connection attempt.")
except Exception as e:
    print(f"Error: {e}")
else:
        print("Connection failed!")

client = mqtt.Client()
client.on_connect = on_connect

try:
    print("Attempting to connect to the MQTT broker...")
    client.connect(broker, port, 60)
    client.loop_start()
    time.sleep(5)  # Wait for connection
    client.loop_stop()
    print("Finished connection attempt.")
except Exception as e:
    print(f"Error: {e}")
