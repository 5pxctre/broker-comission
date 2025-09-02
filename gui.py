import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from app_logic import AppLogic

class App:
    def __init__(self,root, logic: AppLogic):
        self.root = root
        self.logic = logic
        self.root.title("Captracker")
        self.root.geometry('450x350')
        #Setting a theme
        style = ttk.Style(root)
        style.theme_use('vista')

        # Builds Widgets
        self.widget_build()


    def widget_build(self):
        main_frame = ttk.Frame(root)
        main_frame.pack()

        #Making a section of frame
        data_entry= ttk.LabelFrame(main_frame, text= "Data Entry")
        data_entry.grid(row = 0, column = 0)

        #Labels for first frame
        self.closing_date_entry = ttk.Label(data_entry, text = "Closing Date (mm/dd/yy)")
        self.closing_date_entry.grid(row = 0, column = 0)
        self.address_label = ttk.Label(data_entry, text = "Address")
        self.address_label.grid(row = 0, column = 1)
        self.gross_label = ttk.Label(data_entry, text = "$ Gross Earned")
        self.gross_label.grid(row=2,column=0)
        self.party_label = ttk.Label(data_entry, text = "$ Other Parties")
        self.party_label.grid(row = 2, column=1)

        # Entry boxes for data entry
        self.date_entry = Entry(data_entry)
        self.date_entry.grid(row = 1, column = 0)
        self.address_entry = Entry(data_entry, width = 30)
        self.address_entry.grid(row= 1 , column = 1)
        self.gross_entry  = Entry(data_entry)
        self.gross_entry.grid(row = 3, column=0)
        self.party_entry = Entry(data_entry)
        self.party_entry.grid(row = 3, column = 1)  

        #Frame for ClearAll Button
        self.clear_frame = ttk.LabelFrame(main_frame)
        self.clear_frame.grid(row = 4, column = 0, sticky= "news")
        self.clearButton = ttk.Button(main_frame, text = "Clear All", command = self.clearAll)
        self.clearButton.grid(row = 5, column = 0, sticky = "news", padx = 20, pady= 10)

        #Frame for calculate button
        calc_frame = ttk.LabelFrame(main_frame)
        calc_frame.grid(row = 2, column = 0, sticky = "news")
        calcButton = ttk.Button(main_frame, text = "Calculate", command=self.onCalc)
        calcButton.grid(row=3 , column = 0, sticky = "news", padx = 20, pady = 10)


    def clearAll(self):
        self.date_entry.delete(0, tk.END)
        self.party_entry.delete(0, tk.END)
        self.gross_entry.delete(0,tk.END)
        self.address_entry.delete(0,tk.END)

    def onCalc(self):
        date = self.date_entry.get()
        otherParty = self.party_entry.get()
        grossAmt = self.gross_entry.get()
        address = self.address_entry.get()
        messagebox.showinfo("Info", self.logic.entryValidation(date,otherParty,grossAmt))

if __name__ == "__main__":
    logic = AppLogic()
    root = tk.Tk()
    app = App(root , logic)
    root.mainloop()