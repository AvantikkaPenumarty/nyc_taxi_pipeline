import pandas as pd  # Import pandas for data handling
import zipfile        # Import zipfile to read ZIP archives
import io             # Import io to decode bytes to text

def extract_data(zip_path):
    print("Extracting data from ZIP...")  # Notify user

    with zipfile.ZipFile(zip_path, 'r') as z:  # Open ZIP file

        # Filter for .csv files only
        csv_files = [f for f in z.namelist() if f.endswith('.csv')]

        # Handle case where ZIP contains no .csv file
        if not csv_files:
            raise FileNotFoundError("No CSV file found inside the ZIP archive.")

        csv_file = csv_files[0]  # Get the first CSV file

        with z.open(csv_file) as f:
            # Decode bytes to text and handle bad characters
            wrapper = io.TextIOWrapper(f, encoding="latin1", errors="replace")

            # Read the CSV into DataFrame, skipping malformed lines
            return pd.read_csv(wrapper, on_bad_lines="skip")
