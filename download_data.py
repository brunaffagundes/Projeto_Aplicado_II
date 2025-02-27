from dotenv import load_dotenv
import kagglehub
import os
import shutil
from pathlib import Path

# Load environment variables (for Kaggle API credentials)
load_dotenv()

# Create a data directory in the script's location if it doesn't exist
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "data")
os.makedirs(data_dir, exist_ok=True)

# Download the latest version of the dataset
# Available at: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
kaggle_path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
print(f"Downloaded dataset to: {kaggle_path}")

# Get all files in the dataset directory
dataset_files = list(Path(kaggle_path).glob("**/*"))
file_count = 0

# Copy each file to the data directory and delete the original
for file_path in dataset_files:
    if file_path.is_file():
        dest_path = os.path.join(data_dir, file_path.name)
        shutil.copy2(file_path, dest_path)
        file_count += 1
        print(f"Copied: {file_path.name}")

        # Delete the file from kaggle_path
        file_path.unlink()
        print(f"Deleted: {file_path.name}")

print(f"\nSuccessfully copied {file_count} files to {data_dir}")
