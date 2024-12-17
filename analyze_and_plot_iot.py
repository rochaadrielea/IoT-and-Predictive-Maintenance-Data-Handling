import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
DB_PATH = "iot_cleaned_data.db"  # Path to SQLite database
OUTPUT_FOLDER = "plot_iot"       # Folder to save plots
TEMP_THRESHOLD = 70.0            # Temperature threshold for anomalies
VIB_THRESHOLD = 1.5              # Vibration threshold for anomalies

# Function to ensure output folder exists
def init_output_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# Load IoT Data
def load_data(db_path):
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM cleaned_iot_data"
    df = pd.read_sql(query, conn)
    conn.close()
    print("Data loaded successfully!")
    return df

#Clean Data
def clean_data(df):
    """Clean and process DataFrame."""
    print("Cleaning data...")
    # Drop rows where critical columns are missing
    df = df.dropna(subset=["Temperature (C)", "Vibration (mm/s)", "Throughput (units/hour)"])
    # Replace missing values with reasonable defaults
    df.fillna({
        "Temperature (C)": df["Temperature (C)"].median(),
        "Vibration (mm/s)": 0.0,
        "Downtime Log": "None",
        "Throughput (units/hour)": df["Throughput (units/hour)"].mean()
    }, inplace=True)
    # Remove duplicate rows
    df = df.drop_duplicates()
    print("Data cleaned successfully!")
    return df


# Downtime Analysis
def plot_downtime(df, folder):
    """Analyze downtime reasons and create a bar chart."""
    downtime_counts = df['Downtime Log'].value_counts()

    plt.figure(figsize=(8, 5))
    downtime_counts.plot(kind='bar', color='skyblue')
    plt.title("Downtime Log Analysis")
    plt.xlabel("Downtime Reason")
    plt.ylabel("Count")
    output_path = os.path.join(folder, "downtime_analysis.png")
    plt.savefig(output_path)
    print(f"Saved: {output_path}")
    plt.close()

# More analyses fucntion can be done... enjoy

# Main Function
def main():
    # Setup output folder
    init_output_folder(OUTPUT_FOLDER)

    # Load and clean data
    df = load_data(DB_PATH)
    df = clean_data(df)

    #  Generate visualizations
    print("Generating visualizations...")
  
    plot_downtime(df, OUTPUT_FOLDER)

    print(f"All plots saved in '{OUTPUT_FOLDER}' folder.")

if __name__ == "__main__":
    main()
