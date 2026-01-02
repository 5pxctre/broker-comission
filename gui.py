import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from app_logic import AppLogic

class App:
    def __init__(self, root, logic: AppLogic):
        self.root = root
        self.logic = logic
        self.root.title("Captracker")
        self.root.geometry('450x400') 
        
        style = ttk.Style(self.root)
        try:
            style.theme_use('vista')
        except:
            pass 

        self.widget_build()

    def widget_build(self):
        main_frame = ttk.Frame(self.root) 
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        data_entry = ttk.LabelFrame(main_frame, text="Data Entry")
        data_entry.grid(row=0, column=0, sticky="ew")

        ttk.Label(data_entry, text="Closing Date (mm/dd/yy)").grid(row=0, column=0)
        ttk.Label(data_entry, text="Address").grid(row=0, column=1)
        ttk.Label(data_entry, text="$ Gross Earned").grid(row=2, column=0)
        ttk.Label(data_entry, text="$ Other Parties").grid(row=2, column=1)

        self.date_entry = ttk.Entry(data_entry)
        self.date_entry.grid(row=1, column=0, padx=5, pady=5)
        self.address_entry = ttk.Entry(data_entry, width=30)
        self.address_entry.grid(row=1, column=1, padx=5, pady=5)
        self.gross_entry = ttk.Entry(data_entry)
        self.gross_entry.grid(row=3, column=0, padx=5, pady=5)
        self.party_entry = ttk.Entry(data_entry)
        self.party_entry.grid(row=3, column=1, padx=5, pady=5)  

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, pady=20)
        
        ttk.Button(button_frame, text="Calculate & Save", command=self.onCalc).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear All", command=self.clearAll).pack(side="left", padx=5)
        ttk.Button(button_frame, text="View Database", command=self.open_records_window).pack(side="left", padx=5)

    def open_records_window(self):
        records_win = tk.Toplevel(self.root)
        records_win.title("Database Records")
        records_win.geometry("800x300")

        # --- CHANGED: Column name from 'cap' to 'other' ---
        columns = ('id', 'address', 'price', 'split', 'comm', 'other')
        
        tree = ttk.Treeview(records_win, columns=columns, show='headings')
        
        tree.heading('id', text='ID')
        tree.heading('address', text='Address')
        tree.heading('price', text='Gross Price')
        tree.heading('split', text='Split')
        tree.heading('comm', text='Commission')
        # --- CHANGED: Header Title ---
        tree.heading('other', text='Other Parties')
        
        tree.column('id', width=30)
        tree.column('address', width=200)
        tree.column('price', width=80)
        tree.column('split', width=80)
        tree.column('comm', width=80)
        tree.column('other', width=80)
        
        tree.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(records_win, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        data = self.logic.fetch_history()
        
        for row in data:
            tree.insert('', tk.END, values=(
                row['id'], 
                row['address'], 
                row['price'],
                row['split'],
                row['commission'],
                # --- CHANGED: accessing the new 'other_party' column ---
                row['other_party']
            ))

    def clearAll(self):
        self.date_entry.delete(0, tk.END)
        self.party_entry.delete(0, tk.END)
        self.gross_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def onCalc(self):
        date = self.date_entry.get()
        otherParty = self.party_entry.get()
        grossAmt = self.gross_entry.get()
        address = self.address_entry.get()

        try:
            message, split, com, cap = self.logic.entryValidation(date, otherParty, grossAmt, address)
            messagebox.showinfo("Success", f"{message}\nSplit: {split}\nComm: {com}")
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))