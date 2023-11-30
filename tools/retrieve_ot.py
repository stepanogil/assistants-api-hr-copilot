import pyodbc
import os
import csv
from datetime import datetime
from dotenv import load_dotenv

def retrieve_overtime_records(name_of_user):
    """
    Retrieves overtime records and other time types from Azure SQL Database
    """
    # Load environment variables
    load_dotenv()

    # Retrieve database configuration from environment variables
    az_sql_server = os.getenv('AZURE_SQL_SERVER')
    az_sql_database = os.getenv('AZURE_SQL_DATABASE')
    az_sql_username = os.getenv('AZURE_SQL_USERNAME')
    az_sql_password = os.getenv('AZURE_SQL_PASSWORD')
    driver = '{ODBC Driver 18 for SQL Server}'

    # Establish a connection to the database
    cnxn = pyodbc.connect(
        f'DRIVER={driver};SERVER={az_sql_server};PORT=1433;DATABASE={az_sql_database};UID={az_sql_username};PWD={az_sql_password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')

    cursor = cnxn.cursor()

    # Use a parameterized query to prevent SQL injection
    query = "SELECT employee_number, employee_name, date, time_type, hours, amount_php FROM time_data WHERE supervisor_name = ?"
    cursor.execute(query, name_of_user)
    rows = cursor.fetchall()

    # Define CSV file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ot_csv = f"overtime_records_{timestamp}.csv"

    with open(ot_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in cursor.description])  # Writing headers
        for row in rows:
            writer.writerow(row)

    # Close the cursor and connection
    cursor.close()
    cnxn.close()

    return ot_csv   
