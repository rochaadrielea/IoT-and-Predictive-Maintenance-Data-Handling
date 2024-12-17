import os

# Set the path for Kaggle to download the dataset
os.system('kaggle datasets download -d hiimanshuagarwal/predictive-maintenance-dataset -p ./')

# Unzip the downloaded dataset
os.system('unzip -o predictive-maintenance-dataset.zip -d ./')

print("Dataset downloaded and extracted successfully.")
