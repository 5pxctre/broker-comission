import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class App:
    def __init__(self,root):
        self.root = root
        self.root.title("Captracker")
        self.root.geometry('450x350')


    def widget_build(self):
        



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()