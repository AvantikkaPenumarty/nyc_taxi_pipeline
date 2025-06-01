import pandas as pd  # Import pandas for data handling and manipulation
import zipfile        # Import zipfile to work with ZIP archives
import io             # Import io to wrap byte streams as text streams for decoding

def extract_data(zip_path):
    print("Extracting data from ZIP...")  # Inform the user that data extraction is starting

    # Open the ZIP file located at the provided path
    with zipfile.ZipFile(zip_path, 'r') as z:

        # Identify the first CSV file within the ZIP archive
        csv_file = [f for f in z.namelist() if f.endswith('.csv')][0]

        # Open the CSV file in binary mode and decode it safely as a text stream
        with z.open(csv_file) as f:
            wrapper = io.TextIOWrapper(f, encoding="latin1", errors="replace")  # Decode with latin1 and replace problematic characters

            # Read the CSV into a pandas DataFrame
            # 'on_bad_lines="skip"' skips rows that don't match the column structure (like malformed lines)
            return pd.read_csv(wrapper, on_bad_lines="skip")
