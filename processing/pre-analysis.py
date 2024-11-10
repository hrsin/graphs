import pandas as pd
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk

file_path=None
def choose_file():
    global file_path
    file_path = tk.filedialog.askopenfilename(title="Select csv file", filetypes=[("CSV files", "*.csv")])
    if file_path:
        print("File selected: ", file_path)
        app.quit()

def info():
    global file_path
    global data
    if file_path:
        data = pd.read_csv(file_path)
        #prints out the column names
        print("\nData types -------\n", data.dtypes) #data types of each column
        print("\n First 5 rows of data -------\n",data.head()) # prints first 5 rows
        print("\nInfo of data -------\n")
        print(data.info()) #info about datatype of each column, missing values, memory usage
        print("\nDescription of Data -------\n",data.describe()) #summary statistics of numerical columns-count,mean,std,min,max,25%,50%,75%
        print("\nShape of Data -------\n",data.shape) #shape of data
        print("\nMissing values in Dataset -------\n", data.isna().sum()) #missing values in dataset containing NA values
        print(data["CAN1.Fault.FIC"].value_counts())
        print(data["CAN1.Fault.FTC"].value_counts())
        print(data["CAN1.Fault.FTIC"].value_counts()) 
        print(data["CAN1.Fault.FC"].value_counts()) #frequency of values in a column
        print(data.select_dtypes("object").columns) #selecting columns with object datatype 
        print(data["CAN1.Voltage1.Cell_01"].nunique()) #mean of a column
        # print(data.groupby("#some text value to group by")["CAN1.Voltage1.Cell_01"].std()) #grouping data by a column and calculating mean of another column
    """ 
        print("Data duplicated: ", data.duplicated().sum())
        print("Data duplicated rows: ", data[data.duplicated()])
        print("Data duplicated rows: ", data[data.duplicated(keep=False)])
    """
app = tk.Tk()
choose_label = ttk.Label(app, text="Choose the file to process:")
choose_button = ttk.Button(app, text="Choose file", command=choose_file)
app.geometry("200x80")
app.title("Import your csv file")
choose_label.pack(pady=10)
choose_button.pack()
app.mainloop()

info()

