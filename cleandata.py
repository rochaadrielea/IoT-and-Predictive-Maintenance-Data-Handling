import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import sqlite3

def clean_data():
#  Load raw dataset
    file_path = "/mnt/c/Users/adrie/Documents/projectethon/predictive_maintenance_dataset.csv"  # Correct path
    df = pd.read_csv(file_path)

    # Check for Missing Values and Makes a New df called numeric_cols With Just Numbers
    print("Initial Missing Values:\n", df.isnull().sum())
    numeric_cols = df.select_dtypes(include=['number']).columns 
    df[numeric_cols] = df[numeric_cols].interpolate(method='linear')

    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Invalid dates become NaT
   

    # Normalize Numeric Columns, Here we are Using sklearn.preprocessing
    scaler = MinMaxScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    # Rename Columns
    df.columns = [
    "date", "device_id", "failure_flag", "cumulative_usage", 
    "sensor_pressure", "vibration_spike", "error_threshold", 
    "error_count", "power_load", "warning_log1", 
    "warning_log2", "event_trigger"
    ]

    # Save Cleaned Dataset to a CSV
    cleaned_file_path = "/mnt/c/Users/adrie/Documents/projectethon/cleaned_predictive_maintenance.csv"
    df.to_csv(cleaned_file_path, index=False)
    print("Cleaned dataset saved to:", cleaned_file_path)

    #  Load Dataset into SQLite Database, The db_path Is Running in WSL
    db_path = "/mnt/c/Users/adrie/Documents/projectethon/predictive_maintenance.db"
    conn = sqlite3.connect(db_path)
    df.to_sql("maintenance_data", conn, if_exists="replace", index=False)
    print("Dataset loaded into SQLite database.")

    #  Perform SQL Queries
    cursor = conn.cursor()

    #  Count the number of failures just for cheecking 
    query = "SELECT COUNT(*) AS total_failures FROM maintenance_data WHERE failure_flag = 1"
    cursor.execute(query)
    print("Total Failures:", cursor.fetchone()[0])

    # Example Query 2: Find the average cumulative usage for failed devices
    query = """
    SELECT AVG(cumulative_usage) AS avg_usage
    FROM maintenance_data
    WHERE failure_flag = 1
    """

    query = """
    CREATE TABLE failed_devices_usage AS
    SELECT device_id, cumulative_usage, failure_flag
    FROM maintenance_data
    WHERE failure_flag = 1;

    
    """
    query = """
    CREATE TABLE failed_devices_usage AS
    SELECT device_id, cumulative_usage, failure_flag
    FROM maintenance_data
    WHERE failure_flag = 1;

    ALTER TABLE failed_devices_usage
    ADD COLUMN usage_flag TEXT;

    UPDATE failed_devices_usage
    SET usage_flag = CASE 
                    WHEN cumulative_usage > 1000 THEN 'HIGH'
                    ELSE 'LOW'
                 END;

    """

    cursor.execute(query)
    print("Average Cumulative Usage for Failed Devices:", cursor.fetchone()[0])
    print("Columns after renaming:")
    print(df.columns)

   
    
    df.to_sql("cleaned_maintenance_data", conn, if_exists="replace", index=False)  # Store cleaned table
    print("Cleaned dataset loaded into SQLite database as 'cleaned_maintenance_data'.")
    conn.close()


    # Close the database connection
    conn.close()
    print("Database connection closed.")
    return cleaned_file_path