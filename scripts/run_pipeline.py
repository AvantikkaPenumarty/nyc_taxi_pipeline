from extract import extract_data
from transform import transform_data
from load import load_data

if __name__ == "__main__":
    df = extract_data("data/yellow_tripdata_filtered.zip")
    df_clean = transform_data(df)
    load_data(df_clean, "output/nyc_taxi.db")
