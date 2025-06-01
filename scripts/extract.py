import pandas as pd         # Import the pandas library for data manipulation
import zipfile              # Import the zipfile module to handle ZIP archives

def extract_data(zip_path):
    print("Extracting data from ZIP...")  # Notify user that extraction has started
    with zipfile.ZipFile(zip_path) as z:  # Open the ZIP file at the given path
        csv_file = z.namelist()[0]        # Get the name of the first file inside the ZIP
        with z.open(csv_file) as f:       # Open the CSV file inside the ZIP
            return pd.read_csv(f, encoding="latin1")  # Read the CSV using pandas with encoding fix



