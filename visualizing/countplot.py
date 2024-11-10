import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tkinter as tk
import ttkbootstrap as ttk
import tkinter.filedialog as fd

filepath= None
def select_file():
    global filepath
    filepath = fd.askopenfilename(title="Select .CSV file", filetypes=[("CSV files","*.csv")])
    if filepath:
        print("\nFile path Selected-----\n", filepath)
        app.quit()






app = tk.Tk()
btn = ttk.Button(app,text="Select file", command=select_file)
lbl = ttk.Label(app, text="Select the file to plot the frequency bar chart")
lbl.pack(pady=5)
btn.pack(pady=10)
app.title("Plot freqeuency bar chart")
app.geometry("240x120")
app.resizable(True, True)
app.mainloop()