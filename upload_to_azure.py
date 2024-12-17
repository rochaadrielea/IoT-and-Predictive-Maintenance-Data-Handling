from azure.storage.blob import BlobServiceClient
import os
import time

# Connection settings
CONNECTION_STRING = "Your string key"
CONTAINER_NAME = "iot-data"
LOCAL_FILE_PATH = "iot_cleaned_data.db"  # Database file path

# Function to upload file to Azure Blob Storage
def upload_file_to_blob():
    """Upload database file to Azure Blob Storage."""
    try:
        # Create BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        # Create container if it doesn't exist
        if not container_client.exists():
            container_client.create_container()
            print(f"Container '{CONTAINER_NAME}' created successfully.")

        # Upload the file
        blob_client = container_client.get_blob_client(os.path.basename(LOCAL_FILE_PATH))
        with open(LOCAL_FILE_PATH, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"File '{LOCAL_FILE_PATH}' uploaded successfully to container '{CONTAINER_NAME}'.")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

# Function to monitor file updates
def get_last_modified_time(file_path):
    """Get the last modified time of the file."""
    return os.path.getmtime(file_path) if os.path.exists(file_path) else None

# Main Execution - Periodic Upload
if __name__ == "__main__":
    print("Monitoring file changes and uploading to Azure...")
    last_modified_time = get_last_modified_time(LOCAL_FILE_PATH)
    consecutive_no_updates = 0  # Counter for how long file is unchanged
    MAX_NO_UPDATE_CYCLES = 3  # Stop after 3 cycles with no file updates
    UPLOAD_INTERVAL = 2  # Frequency in seconds

    while True:
        current_modified_time = get_last_modified_time(LOCAL_FILE_PATH)

        if current_modified_time != last_modified_time:
            print("File updated. Uploading...")
            success = upload_file_to_blob()
            if success:
                last_modified_time = current_modified_time
                consecutive_no_updates = 0  # Reset counter
        else:
            print("No updates detected.")
            consecutive_no_updates += 1

        if consecutive_no_updates >= MAX_NO_UPDATE_CYCLES:
            print("No file updates detected for a while. Exiting...")
            break

        time.sleep(UPLOAD_INTERVAL)


