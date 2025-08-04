# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:18:37 2020

@author: Lenovo
"""

from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("My Asean Travel Buddy")

window.geometry('350x200')

combo = Combobox(window)

lbl = Label(window, text="Country Visited:")

lbl.grid(column=0, row=0)


combo['values']= ('Indonesia','Malaysia', 'Thailand','Singapore','Cambodia')

selected_item = combo.current(1) #set the selected item
print(selected_item)
combo.grid(column=2, row=0)


lbl2 = Label(window, text="selected_item")

lbl2.grid(column=0, row=3)

combo.get()
window.mainloop()