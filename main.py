import tkinter as tk
from app_logic import AppLogic
from gui import App

if __name__ == "__main__":
    root = tk.Tk()
    logic = AppLogic()
    app = App(root, logic)
    root.mainloop()