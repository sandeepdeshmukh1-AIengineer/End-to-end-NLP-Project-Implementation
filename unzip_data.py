import zipfile
import os

# ✅ Create artifacts directory if it doesn't exist
os.makedirs("artifacts/data", exist_ok=True)

# ✅ Define the source and destination paths
zip_path = os.path.join("data", "dataset.zip")
extract_path = os.path.join("artifacts", "data")

# ✅ Check and unzip
if not os.path.exists(zip_path):
    print("❌ ZIP file not found. Check the path.")
else:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
        print("✅ Dataset unzipped successfully into 'artifacts/data/' folder.")
