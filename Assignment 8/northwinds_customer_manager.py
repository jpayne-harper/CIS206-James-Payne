import csv

def load_customers(file_path):
    """Reads the CSV file and returns a list of customers as tuples."""
    customers = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip the header row
        for row in reader:
            customers.append(tuple(row))  # Store each row as a tuple
    return customers

def display_customers_sorted(customers, sort_index, headers):
    """Displays customers sorted by the given index (company name or contact name)."""
    sorted_customers = sorted(customers, key=lambda x: x[sort_index])  # Sort by given column
    print(f"\n{' | '.join(headers)}")
    print("=" * 90)
    for customer in sorted_customers:
        print(f"{customer[sort_index]:<30} | {customer[1]:<40} | {customer[9]}")

def search_customers(customers, search_term, search_index, headers):
    """Searches customers by company name or contact name."""
    results = [customer for customer in customers if search_term.lower() in customer[search_index].lower()]
    if results:
        print(f"\n{' | '.join(headers)}")
        print("=" * 90)
        for customer in results:
            print(f"{customer[search_index]:<30} | {customer[1]:<40} | {customer[9]}")
    else:
        print("No matching records found.")

def menu(customers):
    """Displays menu options and executes user selections."""
    while True:
        print("\nMenu:")
        print("1. Display customers sorted by company name")
        print("2. Display customers sorted by contact name")
        print("3. Search customers by company name")
        print("4. Search customers by contact name")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_customers_sorted(customers, 1, ["Company Name", "Contact Name", "Phone"])
        elif choice == "2":
            display_customers_sorted(customers, 2, ["Contact Name", "Company Name", "Phone"])
        elif choice == "3":
            search_term = input("Enter company name or part of name: ").strip()
            search_customers(customers, search_term, 1, ["Company Name", "Contact Name", "Phone"])
        elif choice == "4":
            search_term = input("Enter contact name or part of name: ").strip()
            search_customers(customers, search_term, 2, ["Contact Name", "Company Name", "Phone"])
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5.")

if __name__ == "__main__":
    file_path = "Northwinds_customers.csv"  # Update with the actual file path
    customers_list = load_customers(file_path)
    menu(customers_list)
