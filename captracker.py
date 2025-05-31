import math
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def show_message():
    messagebox.showinfo('Message', "Hey there! You are such a cutie patootie")

root = Tk()
main_frame = ttk.Frame(root)
main_frame.pack()
test_button = ttk.Button(main_frame, text = 'Confirm', command=show_message).pack()

num = StringVar()
name = ttk.Entry(root,)



def main():
    gross = inputAlgo("Gross Earned")
    other = inputAlgo("$ Other Parties")
    commission, split = calc(gross, other)


def calc(gross, other):
    com = gross - other
    spl = com * 0.2
    print()
    com = round(com, 2)
    spl = round(spl, 2)
    capCon = spl
    print("Comission: $" + str(com))
    print("Split: $" + str(spl))    
    print("Cap Contribution: $" + str(capCon))
    print()
    return com, spl

def inputAlgo(var):
    print()
    x = input("Input " + var + " : ")
    x = "".join(x.split())
    x = x.replace(",", "")
    if x[0] == "$" and (x.count("$") == 1):
        x = x.replace("$", "")
    if not numCheck(x):
        return inputAlgo()
    return float(x)


def numCheck(x):
    x = x.replace(".", "")
    if not x.isdigit():
        return False
    x = float(x)
    if x >= 0:
        return True
    else:
        return False
    
main()