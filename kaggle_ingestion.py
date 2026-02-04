import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# -----------------------------
# Configuration
# -----------------------------
DATASET_NAME = "olistbr/brazilian-ecommerce"
DOWNLOAD_DIR = "data/raw"
ZIP_FILE_NAME = "olist_dataset.zip"

# -----------------------------
# Create directories if needed
# -----------------------------
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# -----------------------------
# Authenticate Kaggle API
# -----------------------------
api = KaggleApi()
api.authenticate()

print("✅ Kaggle API authenticated")

# -----------------------------
# Download dataset
# -----------------------------
print("⬇️ Downloading Olist dataset from Kaggle...")
api.dataset_download_files(
    DATASET_NAME,
    path=DOWNLOAD_DIR,
    quiet=False,
    unzip=False
)

# -----------------------------
# Locate downloaded zip file
# -----------------------------
zip_path = None
for file in os.listdir(DOWNLOAD_DIR):
    if file.endswith(".zip"):
        zip_path = os.path.join(DOWNLOAD_DIR, file)
        break

if zip_path is None:
    raise FileNotFoundError("❌ Dataset zip file not found")

# Rename zip file (optional but clean)
final_zip_path = os.path.join(DOWNLOAD_DIR, ZIP_FILE_NAME)
os.rename(zip_path, final_zip_path)

print(f"📦 Dataset saved as {final_zip_path}")

# -----------------------------
# Extract zip file
# -----------------------------
print("📂 Extracting dataset...")
with zipfile.ZipFile(final_zip_path, 'r') as zip_ref:
    zip_ref.extractall(DOWNLOAD_DIR)

print("✅ Dataset extracted successfully")

# -----------------------------
# List extracted files
# -----------------------------
print("\n📄 Files extracted:")
for file in os.listdir(DOWNLOAD_DIR):
    if file.endswith(".csv"):
        print(" -", file)

print("\n🎉 Olist dataset is ready for preprocessing!")
