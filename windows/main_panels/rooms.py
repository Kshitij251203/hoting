import tkinter as tk

class Rooms(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.pack(expand=True, fill=tk.BOTH)
