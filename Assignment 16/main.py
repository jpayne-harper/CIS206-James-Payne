import json
import tkinter as tk
from tkinter import messagebox, ttk
from views.data_view import DataView

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        #Setting the Theme for the entire application
        self.style = ttk.Style()
        self.style.theme_use('classic')
        self.geometry("300x150")

        #Window Title
        self.title("Family Tree")


        self.button = tk.Button(self, text="Update Family Tree", command=self.open_toplevel)
        self.button.pack(padx=12, pady=10)

    def open_toplevel(self):
        self.data_view_window = DataView(self)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
