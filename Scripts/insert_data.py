import mysql.connector
import csv
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")

conn = mysql.connector.connect(
    host= host,
    user= user,
    password= password,
    database= database
)

cursor = conn.cursor()

csv_path = os.path.join(os.path.dirname(__file__), "..", "Data",'Walmart.csv')

with open(csv_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    inserted = 0
    skipped = 0

    for row in reader:
        row = [value.strip() for value in row]

        row[1] = datetime.strptime(row[1], "%d-%m-%Y").date()
        cursor.execute("""
            INSERT IGNORE INTO sales (
                Store, Date, Weekly_Sales, Holiday_Flag,
                Temperature, Fuel_Price, CPI, Unemployment
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, row)

        if cursor.rowcount == 1:
            inserted += 1
        else:
            skipped += 1


conn.commit()
cursor.close()
conn.close()

print(f"Done. Inserted: {inserted} rows, Skipped (duplicates): {skipped} rows.")


