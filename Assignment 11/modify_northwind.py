"""
modify_northwind.py
Modify records (Insert, Update, Delete) in the Northwind SQLite database.
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
    """Retrieve all table names from the database."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        return tables
    except sqlite3.Error as e:
        print(f"Error fetching table names: {e}")
        return []

def get_field_names(conn, table_name):
    """Retrieve field names for a given table."""
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    fields = [row[1] for row in cursor.fetchall()]
    return fields

def display_table_records(conn, table_name):
    """Display all records from a selected table with row numbers."""
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()
        field_names = [description[0] for description in cursor.description]

        if not records:
            print(f"No records found in table '{table_name}'.")
            return

        print("\n--- Records ---")
        print("Row | " + " | ".join(field_names))
        print("-" * 50)

        for idx, record in enumerate(records, 1):
            row = f"{idx:<3} | " + " | ".join(str(value) for value in record)
            print(row)
        print("-" * 50)

    except sqlite3.Error as e:
        print(f"Error displaying records: {e}")

def insert_record(conn, table_name):
    """Insert a new record into the table."""
    fields = get_field_names(conn, table_name)
    values = []

    print("\nEnter values for the new record:")
    for field in fields:
        val = input(f"{field}: ").strip()
        values.append(val)

    placeholders = ", ".join(["?"] * len(fields))
    sql = f"INSERT INTO {table_name} ({', '.join(fields)}) VALUES ({placeholders})"

    try:
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        print("Record inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting record: {e}")

def update_record(conn, table_name):
    """Update a field in a selected record."""
    display_table_records(conn, table_name)
    fields = get_field_names(conn, table_name)

    try:
        row_id = int(input("\nEnter the Row number to update: ")) - 1
        field_to_update = input(f"Enter the field to update ({', '.join(fields)}): ").strip()
        if field_to_update not in fields:
            print("Invalid field name.")
            return
        new_value = input("Enter the new value: ").strip()

        cursor = conn.cursor()
        cursor.execute(f"SELECT rowid, * FROM {table_name}")
        records = cursor.fetchall()

        if 0 <= row_id < len(records):
            record_rowid = records[row_id][0]
            sql = f"UPDATE {table_name} SET {field_to_update} = ? WHERE rowid = ?"
            cursor.execute(sql, (new_value, record_rowid))
            conn.commit()
            print("Record updated successfully.")
        else:
            print("Invalid row number.")

    except (ValueError, sqlite3.Error) as e:
        print(f"Error updating record: {e}")

def delete_record(conn, table_name):
    """Delete a selected record from the table."""
    display_table_records(conn, table_name)

    try:
        row_id = int(input("\nEnter the Row number to delete: ")) - 1
        cursor = conn.cursor()
        cursor.execute(f"SELECT rowid, * FROM {table_name}")
        records = cursor.fetchall()

        if 0 <= row_id < len(records):
            record_rowid = records[row_id][0]
            cursor.execute(f"DELETE FROM {table_name} WHERE rowid = ?", (record_rowid,))
            conn.commit()
            print("Record deleted successfully.")
        else:
            print("Invalid row number.")

    except (ValueError, sqlite3.Error) as e:
        print(f"Error deleting record: {e}")

def main():
    """Main program to modify database records."""
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
        choice = int(input("\nSelect a table number to work with: "))
        if 1 <= choice <= len(tables):
            selected_table = tables[choice - 1]
            display_table_records(conn, selected_table)

            while True:
                action = input("\nChoose an action - (I)nsert, (U)pdate, (D)elete, (Q)uit: ").strip().upper()
                if action == "I":
                    insert_record(conn, selected_table)
                elif action == "U":
                    update_record(conn, selected_table)
                elif action == "D":
                    delete_record(conn, selected_table)
                elif action == "Q":
                    print("Exiting program.")
                    break
                else:
                    print("Invalid choice. Please choose I, U, D, or Q.")
        else:
            print("Invalid table selection.")
    except ValueError:
        print("Please enter a valid number.")

    conn.close()

if __name__ == "__main__":
    main()
