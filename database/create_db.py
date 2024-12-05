import sqlite3
import pandas as pd
import os

def create_database():
    # Get the absolute path to the database directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_dir = os.path.join(current_dir, 'database')
    csv_path = os.path.join(db_dir, 'heart_failure.csv')
    db_path = os.path.join(db_dir, 'Heart_failure_db.db')

    # Create database directory if it doesn't exist
    os.makedirs(db_dir, exist_ok=True)

    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Create a connection to the database
    conn = sqlite3.connect(db_path)

    # Create table
    conn.execute('''
    CREATE TABLE IF NOT EXISTS heart_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age INTEGER,
        anaemia INTEGER,
        creatinine_phosphokinase INTEGER,
        diabetes INTEGER,
        ejection_fraction INTEGER,
        high_blood_pressure INTEGER,
        platelets FLOAT,
        serum_creatinine FLOAT,
        serum_sodium INTEGER,
        sex INTEGER,
        smoking INTEGER,
        time INTEGER,
        death_event INTEGER
    )
    ''')

    # Write the data to a sqlite table
    df.to_sql('heart_data', conn, if_exists='replace', index=False)

    # Commit changes and close connection
    conn.commit()
    conn.close()
    print(f"Database created successfully at: {db_path}")

if __name__ == '__main__':
    create_database()
