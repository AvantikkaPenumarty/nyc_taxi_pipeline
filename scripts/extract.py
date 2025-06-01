import pandas as pd
import zipfile

def extract_data(zip_path):
    print("Extracting Excel file from ZIP...")

    with zipfile.ZipFile(zip_path) as z:
        # Get the first Excel file inside the ZIP
        xlsx_files = [f for f in z.namelist() if f.endswith('.xlsx')]
        if not xlsx_files:
            raise FileNotFoundError("No Excel file found inside the ZIP archive.")
        xlsx_file = xlsx_files[0]

        # Read it using pandas
        with z.open(xlsx_file) as f:
            return pd.read_excel(f)  # Use read_excel instead of read_csv

