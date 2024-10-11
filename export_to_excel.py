import sqlite3
import pandas as pd

# Function to export data from SQLite to Excel
def export_to_excel(db_file='warehouse.db', excel_file='warehouse_data.xlsx'):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)

    # List of tables to export
    tables = ['Suppliers', 'Products', 'Customers', 'Orders']

    # Create a Pandas Excel writer using Openpyxl as the engine
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        for table in tables:
            # Read the table into a DataFrame
            df = pd.read_sql_query(f'SELECT * FROM {table}', conn)
            # Write the DataFrame to the Excel file, with each table in a separate sheet
            df.to_excel(writer, sheet_name=table, index=False)

    # Close the database connection
    conn.close()
    print(f'Data exported to {excel_file} successfully!')

# Call the function to export data
if __name__ == "__main__":
    export_to_excel()
