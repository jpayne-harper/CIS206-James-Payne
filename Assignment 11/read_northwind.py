"""
read_northwind.py
Reads tables and displays records from the Northwind SQLite database.
Python 3.7.3 Compatible.
"""

import sqlite3

def connect_to_database(db_path):
    """Connect to the SQLite database."""
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def get_table_names(conn):
    """Retrieve the names of all tables in the database."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        return tables
    except sqlite3.Error as e:
        print(f"Error fetching table names: {e}")
        return []

def get_field_names(cursor):
    """Retrieve the field names from the cursor description."""
    return [description[0] for description in cursor.description]

def display_table_records(conn, table_name):
    """Display all records from a selected table with headers and row numbers."""
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()
        field_names = get_field_names(cursor)

        if not records:
            print(f"No records found in table '{table_name}'.")
            return

        # Determine column widths
        col_widths = [len(field) for field in field_names]
        for record in records:
            for i, value in enumerate(record):
                col_widths[i] = max(col_widths[i], len(str(value)))

        # Display header
        header = "Row | " + " | ".join(field.ljust(col_widths[i]) for i, field in enumerate(field_names))
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        # Display rows
        for idx, record in enumerate(records, 1):
            row = f"{idx:<3} | " + " | ".join(str(value).ljust(col_widths[i]) for i, value in enumerate(record))
            print(row)
        print("-" * len(header))

    except sqlite3.Error as e:
        print(f"Error displaying records: {e}")

def main():
    """Main program to interact with the database."""
    db_path = input("Enter the full path to your Northwind database file: ").strip()

    conn = connect_to_database(db_path)
    if not conn:
        return

    tables = get_table_names(conn)
    if not tables:
        print("No tables found.")
        return

    print("\nAvailable Tables:")
    for idx, table in enumerate(tables, 1):
        print(f"{idx}. {table}")

    try:
        choice = int(input("\nSelect a table number to view its records: "))
        if 1 <= choice <= len(tables):
            selected_table = tables[choice - 1]
            display_table_records(conn, selected_table)
        else:
            print("Invalid table selection.")
    except ValueError:
        print("Please enter a valid number.")

    conn.close()

if __name__ == "__main__":
    main()
