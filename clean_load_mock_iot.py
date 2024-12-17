import pandas as pd
import sqlite3

# Paths
input_file = "mock_iot_data.csv"
db_file = "iot_cleaned_data.db"

# Load Data
def load_data(file_path):
    print("Loading data...")
    return pd.read_csv(file_path)

# Clean Data
def clean_data(df):
    print("Cleaning data...")
    # Drop completely empty rows
    df = df.dropna(how="all")
    
    # Drop rows where "Downtime Log" is NaN
    df = df.dropna(subset=["Downtime Log"])
    
    # Replace values in "Downtime Log" column
    df["Downtime Log"] = df["Downtime Log"].apply(
        lambda x: 0 if "everything" in str(x).lower() else 1
    )
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    print("Cleaning completed!")
    return df


# Save to SQLite
def save_to_sqlite(df, db_path):
    print("Saving data to SQLite...")
    conn = sqlite3.connect(db_path)
    df.to_sql("cleaned_iot_data", conn, if_exists="replace", index=False)
    conn.close()
    print("Data saved to SQLite successfully!")

# Main execution
if __name__ == "__main__":
    # Load and clean data
    df = load_data(input_file)
    print("Original Data:")
    print(df.head())
    
    cleaned_df = clean_data(df)
    print("Cleaned Data:")
    print(cleaned_df.head())

    # Save to SQLite
    save_to_sqlite(cleaned_df, db_file)
