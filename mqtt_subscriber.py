import paho.mqtt.client as mqtt
import pandas as pd
import sqlite3
from datetime import datetime
import re

# MQTT Configuration
broker = "broker.hivemq.com"
port = 1883
topic = "iot/sensor/data"

# Database Path
DB_PATH = "iot_cleaned_data.db"

# Initialize SQLite Database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cleaned_iot_data (
            Timestamp TEXT,
            Temperature REAL,
            Vibration REAL,
            Downtime TEXT,
            Throughput INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Function to Parse Payload
def parse_payload(payload):
    """Extract values from payload string using regex."""
    try:
        temp_match = re.search(r"Temperature: ([\d.]+)", payload)
        vib_match = re.search(r"Vibration: ([\d.]+)", payload)
        downtime_match = re.search(r"Downtime: (\d+)", payload)
        throughput_match = re.search(r"Throughput: (\d+)", payload)


        # Parse values
        temperature = float(temp_match.group(1)) if temp_match else None
        vibration = float(vib_match.group(1)) if vib_match else 0.0
        downtime = downtime_match.group(1) if downtime_match else "None"
        throughput = int(throughput_match.group(1)) if throughput_match else 0

        # Add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "Timestamp": timestamp,
            "Temperature (C)": temperature,
            "Vibration (mm/s)": vibration,
            "Downtime Log": downtime,
            "Throughput (units/hour)": throughput
        }
    except Exception as e:
        print(f"Error parsing payload: {e}")
        return None
    

# Clean Data Function
def clean_data(df):
    """Clean and process DataFrame."""
    print("Cleaning data...")
    df = df.dropna(how='all')  # Drop completely empty rows
    df.fillna({
    "Temperature (C)": df["Temperature (C)"].median(),
    "Vibration (mm/s)": 0.0,
    "Downtime Log": "None",
    "Throughput (units/hour)": df["Throughput (units/hour)"].mean() }, inplace=True)
    df = df.drop_duplicates()
    print("Data cleaned successfully!")
    return df

# Callback to Process and Store Data
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"Received: {payload}")

    # Parse the payload
    parsed_data = parse_payload(payload)
    if parsed_data:
        try:
            # Convert to DataFrame for cleaning
            df = pd.DataFrame([parsed_data])
            cleaned_df = clean_data(df)

            # Insert into SQLite database
            conn = sqlite3.connect(DB_PATH)
            cleaned_df.to_sql("cleaned_iot_data", conn, if_exists="append", index=False)
            conn.close()
            print(f"Inserted: {cleaned_df.to_dict(orient='records')}")
        except Exception as e:
            print(f"Error inserting data: {e}")

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully!")
        client.subscribe(topic)
    else:
        print(f"Connection failed with code {rc}")

# Main Function
def main():
    init_db()  # Initialize database

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    print("Connecting to MQTT broker and listening...")
    client.connect(broker, port, 60)

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("Stopped by user.")
        client.disconnect()

if __name__ == "__main__":
    main()
