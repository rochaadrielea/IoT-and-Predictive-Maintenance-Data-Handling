import numpy as np
import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker for downtime simulation
fake = Faker()

# Generate IoT Data
def generate_iot_data(num_records=100):
    data = []
    start_time = datetime.now()
    
    for _ in range(num_records):
        timestamp = start_time.strftime("%Y-%m-%d %H:%M:%S")
        temperature = round(np.random.uniform(50.0, 100.0), 2)  # °C
        vibration = round(np.random.uniform(0.1, 2.0), 2)       # mm/s
        downtime = random.choice([fake.word(), "None"])         # Random downtime
        throughput = random.randint(0, 100)                  # Units per hour
        
        data.append({
            "Timestamp": timestamp,
            "Temperature (C)": temperature,
            "Vibration (mm/s)": vibration,
            "Downtime Log": downtime,
            "Throughput (units/hour)": throughput
        })
        start_time += timedelta(seconds=10)  # Increment time by 10 seconds
    
    return data

# Save data to CSV
def save_to_csv(data, file_name="mock_iot_data.csv"):
    print("Saving data to CSV...")
    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)
    print(f"Data saved to {file_name}")

# Main execution
if __name__ == "__main__":
    num_records = 500  # Number of records to generate
    iot_data = generate_iot_data(num_records)
    save_to_csv(iot_data)

