# Tool Usage - Step-by-Step Instructions

## 1. Environment Setup

### Create Virtual Environment:

python3 -m venv project_ethon
source project_ethon/bin/activate

### Install Dependencies:

pip install -r requirements.txt

** File Link** 
   - [requirements.txt](requirements.txt)

###  Process Kaggle Dataset
Download Dataset
python kaggle_database.py

** File Link** 
   - [kaggle_database.py](kaggle_database.py)

Clean Kaggle Data
python cleandata.py

** File Link** 
   - [cleandata.py](cleandata.py)

###  Analyze and Visualize Kaggle Data

python data_analyses.py

** File Link** 
   - [data_analyses.py](data_analyses.py)

###  Process IoT Mock Data

### IF IS THE FIRST TIME please run
Generate Mock IoT Data
python archive/mock_IoT.py


** File Link** 
   - [archive/mock_IoT.py](archive/mock_IoT.py)

### IF IS THE FIRST TIME please run

Clean Mock IoT Data
    python clean_load_mock_iot.py

** File Link** 
   - [clean_load_mock_iot.py](clean_load_mock_iot.py)

###  Publish IoT Data to MQTT Broker

python mqtt_publisher.py

** File Link** 
   - [mqtt_publisher.py](mqtt_publisher.py)

###  Subscribe and Store IoT Data in SQLite

python mqtt_subscriber.py

** File Link** 
   - [mqtt_subscriber.py](mqtt_subscriber.py)
###  Analyze and Visualize IoT Data

python analyze_and_plot_iot.py

** File Link** 
   - [analyze_and_plot_iot.py](analyze_and_plot_iot.py)
### Upload IoT Cleaned Data to Azure

python upload_to_azure.py
** File Link** 
   - [upload_to_azure.py](upload_to_azure.py)
###  Verify Databases on bash

predictive-maintenance.db

** File Link** 
   - [sqlitequery_kaggle.sql](sqlitequery_kaggle.sql)



iot_cleaned_data.db
** File Link** 
   - [sqlitequery_iot.sql](sqlitequery_iot.sql)


###   Review Visualizations
Kaggle Plots: Check the folder plots/
IoT Plots: Check the folder plot_iot/

