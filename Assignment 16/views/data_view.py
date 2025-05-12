import json
import tkinter as tk
from tkinter import messagebox
from logic.formatting import add_family_member_logic, generate_family_report


class DataView(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Create/Update/Delete Data")

        # Input Fields
        tk.Label(self, text="First Name:").grid(row=0, column=0, sticky="e")
        self.entry_first_name = tk.Entry(self)
        self.entry_first_name.grid(row=0, column=1)

        tk.Label(self, text="Last Name:").grid(row=1, column=0, sticky="e")
        self.entry_last_name = tk.Entry(self)
        self.entry_last_name.grid(row=1, column=1)

        tk.Label(self, text="Suffix:").grid(row=2, column=0, sticky="e")
        self.entry_suffix = tk.Entry(self)
        self.entry_suffix.grid(row=2, column=1)

        tk.Label(self, text="Alive (Yes/No):").grid(row=3, column=0, sticky="e")
        self.alive_var = tk.StringVar(value="Yes")
        self.entry_alive = tk.OptionMenu(self, self.alive_var, "Yes", "No")
        self.entry_alive.grid(row=3, column=1)

        tk.Label(self, text="Father's Name:").grid(row=4, column=0, sticky="e")
        self.entry_father = tk.Entry(self)
        self.entry_father.grid(row=4, column=1)

        tk.Label(self, text="Mother's Name:").grid(row=5, column=0, sticky="e")
        self.entry_mother = tk.Entry(self)
        self.entry_mother.grid(row=5, column=1)

        tk.Label(self, text="Year of Birth:").grid(row=6, column=0, sticky="e")
        self.entry_birth_year = tk.Entry(self)
        self.entry_birth_year.grid(row=6, column=1)

        # Submit and View Buttons
        self.submit_btn = tk.Button(self, text="Add Member", command=self.add_family_member)
        self.submit_btn.grid(row=7, column=0, pady=10)

        self.view_btn = tk.Button(self, text="View Data", command=self.display_family_data)
        self.view_btn.grid(row=7, column=1, pady=10)

        # Text box for displaying output
        self.output_box = tk.Text(self, height=15, width=60)
        self.output_box.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def clear_fields(self):
        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_suffix.delete(0, tk.END)
        self.alive_var.set("Yes")  # Reset dropdown to default
        self.entry_father.delete(0, tk.END)
        self.entry_mother.delete(0, tk.END)
        self.entry_birth_year.delete(0, tk.END)

    def add_family_member(self):
        data = {
            "first_name": self.entry_first_name.get(),
            "last_name": self.entry_last_name.get(),
            "suffix": self.entry_suffix.get(),
            "alive": self.alive_var.get(),
            "father": self.entry_father.get(),
            "mother": self.entry_mother.get(),
            "year_of_birth": self.entry_birth_year.get()
        }
        success, msg = add_family_member_logic(data)
        if success:
            messagebox.showinfo("Success", msg)
            self.display_single_entry(data)
            self.clear_fields()
        else:
            messagebox.showerror("Input Error", msg)

    def display_family_data(self):
        self.output_box.delete("1.0", tk.END)
        report = generate_family_report()
        self.output_box.insert(tk.END, report)

    def display_single_entry(self, entry_data):
        """Display only the most recently added member in the output box."""
        self.output_box.delete("1.0", tk.END)

        full_name = f"{entry_data['first_name']} {entry_data['last_name']} {entry_data['suffix']}".strip()
        year = entry_data.get('year_of_birth', '?')
        alive = entry_data['alive']
        father = entry_data['father']
        mother = entry_data['mother']

        line = (
            f"{full_name}\n"
            f" - Born: {year}\n"
            f" - Alive: {alive}\n"
            f" - Father: {father}\n"
            f" - Mother: {mother}\n"
        )
        self.output_box.insert(tk.END, line)

