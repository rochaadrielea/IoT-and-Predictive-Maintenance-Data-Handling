import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import numpy as np
import os  # To handle the directory creation
import pandas as pd
import sqlite3


def run_data_analyses():
    # Load data from the cleaned table in SQLite
    db_path = "/mnt/c/Users/adrie/Documents/projectethon/predictive_maintenance.db"
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM cleaned_maintenance_data"
    df = pd.read_sql_query(query, conn)

    # Summary statistics
    print("Data Info:")
    print(df.info())
    print("\nSummary Statistics:")
    print(df.describe())

    # Display the first 5 rows
    print("\nFirst 5 Rows of Data (First 5 Columns):")
    print(df.iloc[:, :5].head())

    # Create the "plots" folder if it doesn't exist
    if not os.path.exists('plots'):
        os.makedirs('plots')

    # Plot failure_flag distribution
    plt.figure(figsize=(6, 4))
    sns.countplot(x="failure_flag", data=df)
    plt.title("Failure Flag Distribution")
    plt.savefig("plots/failure_flag_distribution.png")
    plt.close()
  # More analyses can be done... enjoy
     

    print("Data analyses and visualizations complete. Plots saved in 'plots' folder.")
    conn.close()
