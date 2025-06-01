import pandas as pd
import zipfile

def extract_data(zip_path):
    print("Extracting data from ZIP...")
    with zipfile.ZipFile(zip_path) as z:
        csv_file = z.namelist()[0]
        with z.open(csv_file) as f:
            return pd.read_csv(f)

