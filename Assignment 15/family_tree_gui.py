import json
import tkinter as tk
from tkinter import messagebox

# File path to JSON family tree
JSON_FILE = 'family_tree.json'

# Load current family data or return an empty template
def load_family_data():
    try:
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"family": []}

# Save updated data back to JSON
def save_family_data(data):
    with open(JSON_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# Function triggered when "Add Member" button is clicked
def add_family_member():
    # Get input values from form
    first_name = entry_first_name.get().strip()
    last_name = entry_last_name.get().strip()
    suffix = entry_suffix.get().strip()
    alive_str = alive_var.get()
    father = entry_father.get().strip()
    mother = entry_mother.get().strip()
    year_of_birth = entry_birth_year.get().strip()

    # Basic validation
    if not first_name or not last_name:
        messagebox.showerror("Input Error", "First and last name are required.")
        return

    if not year_of_birth.isdigit():
        messagebox.showerror("Input Error", "Year of birth must be a numeric value.")
        return

    # Convert alive field to Boolean
    alive = True if alive_str == "Yes" else False

    # String manipulation: Combine full name
    full_name = f"{first_name} {last_name} {suffix}".strip()

    # Load existing data and append new member
    data = load_family_data()
    data["family"].append({
        "first_name": first_name,
        "last_name": last_name,
        "suffix": suffix,
        "alive": alive,
        "father": father,
        "mother": mother,
        "year_of_birth": int(year_of_birth),
        "full_name": full_name
    })
    save_family_data(data)

    messagebox.showinfo("Success", f"{full_name} added to the family tree!")

# Function to display existing family data in a text widget
def display_family_data():
    data = load_family_data()
    output_box.delete("1.0", tk.END)
    if not data["family"]:
        output_box.insert(tk.END, "No family members in the file.")
        return
    for person in data["family"]:
        line = f"{person['full_name']}\n - Born: {person.get('year_of_birth', '?')}\n - Alive: {person['alive']}"
        line += f" - Father: {person['father']}\n - Mother: {person['mother']}\n"
        output_box.insert(tk.END, line)

# GUI window setup
root = tk.Tk()
root.title("Family Tree Entry Form")

# Input Fields
tk.Label(root, text="First Name:").grid(row=0, column=0, sticky="e")
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1)

tk.Label(root, text="Last Name:").grid(row=1, column=0, sticky="e")
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1)

tk.Label(root, text="Suffix:").grid(row=2, column=0, sticky="e")
entry_suffix = tk.Entry(root)
entry_suffix.grid(row=2, column=1)

tk.Label(root, text="Alive (Yes/No):").grid(row=3, column=0, sticky="e")
alive_var = tk.StringVar(value="Yes")
entry_alive = tk.OptionMenu(root, alive_var, "Yes", "No")
entry_alive.grid(row=3, column=1)

tk.Label(root, text="Father's Name:").grid(row=4, column=0, sticky="e")
entry_father = tk.Entry(root)
entry_father.grid(row=4, column=1)

tk.Label(root, text="Mother's Name:").grid(row=5, column=0, sticky="e")
entry_mother = tk.Entry(root)
entry_mother.grid(row=5, column=1)

tk.Label(root, text="Year of Birth:").grid(row=6, column=0, sticky="e")
entry_birth_year = tk.Entry(root)
entry_birth_year.grid(row=6, column=1)

# Submit and View Buttons
submit_btn = tk.Button(root, text="Add Member", command=add_family_member)
submit_btn.grid(row=7, column=0, pady=10)

view_btn = tk.Button(root, text="View Data", command=display_family_data)
view_btn.grid(row=7, column=1, pady=10)

# Text box for displaying output
output_box = tk.Text(root, height=15, width=60)
output_box.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI application
root.mainloop()
