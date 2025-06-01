import sqlite3

def load_data(df, db_file):
    print("Loading data into SQLite DB...")
    conn = sqlite3.connect(db_file)
    df.to_sql("taxi_data", conn, if_exists='replace', index=False)
    conn.close()
