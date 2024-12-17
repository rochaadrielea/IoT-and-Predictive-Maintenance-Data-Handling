import paho.mqtt.client as mqtt
import time
import random

broker = "broker.hivemq.com"
port = 1883

def generate_sensor_data():
    return {
        "temperature": round(random.uniform(20.0, 80.0), 2),
        "vibration": round(random.uniform(0.1, 2.0), 2),
        "downtime": random.choice([0, 1]),
        "throughput": random.randint(50, 100)
    }

client = mqtt.Client()
client.connect(broker, port, 60)

try:
    while True:
        data = generate_sensor_data()
        payload = f"Temperature: {data['temperature']}°C, Vibration: {data['vibration']}g, Downtime: {data['downtime']}, Throughput: {data['throughput']} units"
        client.publish("iot/sensor/data", payload)  # Correct usage
        print(f"Published: {payload}")
        time.sleep(2)
except KeyboardInterrupt:
    print("Stopped publishing.")
    client.disconnect()
