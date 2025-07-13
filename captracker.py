import math
import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk



def show_message(date, third, grossEnt):
    if dateCheck(date):
        if numCheck(grossEnt):
            grossEnt = numCheck(grossEnt)
            if numCheck(third):
                third = numCheck(third)
                calc(grossEnt, third)
            else:
                messagebox.showinfo("Info", "Incorrect Format: $ Other Parties")
        else:
            messagebox.showinfo("Info", "Incorrect Format: Gross Earned")
    else:
        messagebox.showinfo("Info", "Incorrect Format: Closing Date")

def clearAll():
    date_entry.delete(0, tk.END)
    party_input.delete(0, tk.END)
    gross_earned.delete(0,tk.END)

def calc(gross, other):
    com = gross - other
    spl = com * 0.2
    print()
    com = round(com, 2)
    spl = round(spl, 2)
    capCon = spl
    top = Toplevel(root)
    top.title("Calculation Results")
    top.geometry("350x250")
    Label(top, text = "Calculation Result: ").pack(pady = 5)
    Label(top, text= "Closing date: " + date_entry.get()).pack(pady=5)
    Label(top, text = "Address: " + address_entry.get()).pack(pady = 5)
    Label(top, text = "Total Comission: $" + str(com)).pack(pady = 5)    
    Label(top, text = "Cap Split: $" + str(spl)).pack(pady = 5)
    Label(top, text = "Cap Contribution: $" + str(capCon)).pack(pady = 5)

def numCheck(x):
    x = "".join(x.split())
    x = x.replace(",", "")
    if x[0] == "$" and (x.count("$") == 1):
        x = x.replace("$", "")
    x = x.replace(".", "")
    if not x.isdigit():
        return False
    x = float(x)
    if x >= 0:
        return x
    else:
        return False
    
def dateCheck(str):
    try: 
        datetime.datetime.strptime(str, "%m/%d/%y")
        return True
    except:
        return False

def main():
    print("Go")
    
main()

# Make tkinter object
root = Tk()
# Titling the frame
root.title("Captracker")
# Sets size of the object
root.geometry('500x350')
#Setting a theme
style = ttk.Style(root)
style.theme_use('vista')

#Making a frame
main_frame = ttk.Frame(root)
main_frame.pack()

#Making a section of frame
data_entry= ttk.LabelFrame(main_frame, text= "Data Entry")
data_entry.grid(row = 0, column = 0)


#Labels for first frame
closing_date_entry = ttk.Label(data_entry, text = "Closing Date (mm/dd/yy)")
closing_date_entry.grid(row = 0, column = 0)
address_label = ttk.Label(data_entry, text = "Address")
address_label.grid(row = 0, column = 1)
gross_label = ttk.Label(data_entry, text = "$ Gross Earned")
gross_label.grid(row=2,column=0)
party_label = ttk.Label(data_entry, text = "$ Other Parties")
party_label.grid(row = 2, column=1)

# Entry boxes for data entry
date_entry = Entry(data_entry)
date_entry.grid(row = 1, column = 0)
address_entry = Entry(data_entry, width = 30)
address_entry.grid(row= 1 , column = 1)
gross_earned = Entry(data_entry)
gross_earned.grid(row = 3, column=0)
party_input = Entry(data_entry)
party_input.grid(row = 3, column = 1)   


#Frame for Calculation button
calc_frame = ttk.LabelFrame(main_frame)
calc_frame.grid(row = 2, column = 0, sticky = "news")
calcButton = ttk.Button(main_frame, text = "Calculate", command=lambda : show_message(date_entry.get(), party_input.get(), gross_earned.get()))
calcButton.grid(row=3 , column = 0, sticky = "news", padx = 20, pady = 10)

#Frame for ClearAll Button
clear_frame = ttk.LabelFrame(main_frame)
clear_frame.grid(row = 4, column = 0, sticky= "news")
clearButton = ttk.Button(main_frame, text = "Clear All", command = clearAll)
clearButton.grid(row = 5, column = 0, sticky = "news", padx = 20, pady= 10)

for widget in data_entry.winfo_children():
    widget.grid_configure(padx = 5, pady = 5)


root.mainloop()
