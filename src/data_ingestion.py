import pandas as pd
import os

# ----------------------------------
# RAW DATA PATH (UPDATED)
# ----------------------------------
RAW_DATA_PATH = "data"

# ----------------------------------
# FILE NAMES
# ----------------------------------
FILES = {
    "customers": "customers.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "order_payments": "order_payments.csv",
    "products": "products.csv",
    "sellers": "sellers.csv",
    "geolocation": "geolocation.csv",
    "order_reviews": "order_reviews.csv",
    "category_translation": "product_category_name_translation.csv"
}

def load_raw_data(data_path=RAW_DATA_PATH):
    data = {}

    print("📥 Starting data ingestion...\n")

    for key, file_name in FILES.items():
        file_path = os.path.join(data_path, file_name)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ File not found: {file_path}")

        df = pd.read_csv(file_path)
        data[key] = df

        print(f"✅ Loaded {file_name} | Shape: {df.shape}")

    print("\n🎉 All datasets loaded successfully")
    return data


if __name__ == "__main__":
    dataframes = load_raw_data()
