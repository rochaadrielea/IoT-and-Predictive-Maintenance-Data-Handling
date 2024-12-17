import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import numpy as np

# Step 1: Load data from SQLite
conn = sqlite3.connect("predictive_maintenance.db")
query = "SELECT * FROM maintenance_data"
df = pd.read_sql_query(query, conn)

# Step 2: Summary statistics
print("Data Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Display the first 5 columns of the data
print("\nFirst 5 Rows of Data (First 5 Columns):")
print(df.iloc[:, :5].head())  # Shows the first 5 columns

# Step 3: Check failure_flag counts
plt.figure(figsize=(6, 4))
sns.countplot(x="failure_flag", data=df)
plt.title("Failure Flag Distribution")
plt.savefig("failure_flag_distribution.png")  # Save the plot
plt.close()

# Step 4: Correlation heatmap
# Ensure that only numeric columns are considered for correlation
df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Convert 'date' to datetime (if it exists)
df['date'] = df['date'].astype(int, errors='ignore')  # Convert to numeric timestamp (if 'date' exists)

# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=[np.number])

# Drop rows with NaN values (optional)
numeric_df = numeric_df.dropna()

plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.savefig("correlation_heatmap.png")  # Save the plot
plt.close()

# Step 5: Line plot for sensor pressure over time (if date exists)
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"])  # Convert to datetime if 'date' exists
    df.sort_values("date", inplace=True)  # Sort data by date
    plt.figure(figsize=(12, 6))
    plt.plot(df["date"], df["sensor_pressure"], label="Sensor Pressure")
    plt.plot(df["date"], df["vibration_spike"], label="Vibration Spike")
    plt.title("Sensor Pressure and Vibration Spike Over Time")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.savefig("sensor_pressure_vibration_spike_over_time.png")  # Save the plot
    plt.close()

# Close the database connection
conn.close()
