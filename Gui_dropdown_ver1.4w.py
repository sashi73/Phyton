# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 00:06:55 2020

@author: Lenovo
"""

#importing key libraries
import tkinter as tk
from tkinter import  IntVar 
from tkinter import ttk
import datetime
import os

#defining list and in some cases they are empty to be filled in later
countries = ['Brunei',
             'Cambodia',
             'Indonesia',
             'Laos',
             'Malaysia',
             'Myanmar',
             'Philipinies',
             'Singapore',
             'Thailand',
             'Laos',
             'Vietnam']

year_visited =['']
 
def Current_Year(current_year):
    current_year = current_year.year
    current_year = current_year + 1
    print (current_year)
    return(current_year)

#quit the program
def close_window (): 
    app.destroy()
   

#check results
def Save_Next(): 
    print ("Visited country:", comboCountry.get() )
    print ("Visted Year:", comboYear.get())
    if choice_diving.get() == 1:
       print ("Known for diving") 
    if choice_leisure.get() == 1:
       print ("Known for leisure")           
    if choice_food.get() == 1:
       print ("Known for food")
    if choice_shopping.get() == 1:
       print ("Known for shopping")
    if choice_temples.get() == 1:
       print ("Known for temples")
    if choice_beach.get() == 1:
       print ("Known for beach")  
    if choice_liquor.get() == 1:
       print ("Known for liquor") 
    if choice_nature.get() == 1:
       print ("Known for nature")  
    Clear_New()
  
       
       
# clear selection for entering a new choice       
def Clear_New():
    comboCountry.current(4)
    comboYear.current(0)
    choice_diving.set(0)
    choice_leisure.set(0)
    choice_food.set(0)
    choice_shopping.set(0)
    choice_temples.set(0)
    choice_beach.set(0)
    choice_liquor.set(0)
    choice_nature.set(0)
    
    
def New_Window():
      summary_window = tk.Toplevel(app)    
      summary_window.geometry('480x400')
      summary_window.title('My Asean Travel Buddy - Summary')
      summary_window.resizable(0,0)
      sort_by_year = tk.Button (summary_window, text='Sort By Year', bg='green',
                                fg='white', command='', width=10)
      sort_by_year.place(x=350,y=350)
      #sort_by_year.grid (column=1,row=2,sticky=tk.N+tk.W) 
      
    
# initiazlizing tkinter framework for GUI
app = tk.Tk() 
# window size W * H
app.geometry('480x180')
# Window title
app.title('My Asean Travel Buddy')
app.resizable(0,0)
next_year = Current_Year(datetime.datetime.now())


year = range(1920,next_year)
for yearenumator in year:
    year_visited.append(yearenumator)

year_visited.pop(0)

year_visited.sort(reverse=True)


labelCountry = tk.Label(app,
                    text = "Which Country did you visit:",width =25,
                    anchor='w')


   
    
labelCountry.grid(column=0, row=0)

comboCountry = IntVar()
comboCountry = ttk.Combobox(app, 
                            values=countries,
                            state="readonly")

comboCountry.grid(column=3, row=0)
comboCountry.current(4)

labelYear = tk.Label(app,
                    text = "When did you visit the country:", 
                    width =24,
                     padx=0,
                     pady=0)
labelYear.grid(column=0, row=3, sticky=tk.N+tk.W)


comboYear = ttk.Combobox(app, 
                            values=year_visited,
                            state="readonly", width=20)

comboYear.grid(column=3, row=3)
comboYear.current(0)

famous_for = tk.Label(app,
                    text = "What is it famous for:",
                    width=24,
                    anchor='w')
famous_for.grid(column=0, row=4,sticky=tk.N+tk.W)




choice_diving = IntVar()
checkfamous = tk.Checkbutton(app, text = "Diving", variable = choice_diving,  
                              onvalue = 1, offvalue = 0, width = 5
                              )
checkfamous.grid(column=0,row=5,sticky=tk.N+tk.W )

choice_leisure = IntVar()
checkfamous = tk.Checkbutton(app, text = "Leisure", variable = choice_leisure,  
                              onvalue = 1, offvalue = 0, width =5, 
                              anchor='w')
checkfamous.grid(column=0,row=6,sticky=tk.N+tk.W )


choice_food = IntVar()
checkfamous = tk.Checkbutton(app, text = "Food", variable = choice_food,  
                              onvalue = 1, offvalue = 0, width =5, 
                              anchor='w')
checkfamous.grid(column=0,row=7,sticky=tk.N+tk.W )


choice_shopping = IntVar()
checkfamous = tk.Checkbutton(app, text = "Shopping", variable = choice_shopping,  
                              onvalue = 1, offvalue = 0, width = 7
                              )
checkfamous.grid(column=0,row=8,sticky=tk.N+tk.W )

choice_temples = IntVar()
checkfamous = tk.Checkbutton(app, text = "Temples", variable = choice_temples,  
                              onvalue = 1, offvalue = 0, width = 6
                              )
checkfamous.grid(column=0,row=5,sticky=tk.N+tk.E )

choice_beach = IntVar()
checkfamous = tk.Checkbutton(app, text = "Beach", variable = choice_beach,  
                              onvalue = 1, offvalue = 0, width = 8
                              )
checkfamous.grid(column=0,row=6,sticky=tk.N+tk.E )

choice_liquor = IntVar()
checkfamous = tk.Checkbutton(app, text = "Beer ", variable = choice_liquor,  
                              onvalue = 1, offvalue = 0, width = 9
                              )
checkfamous.grid(column=0,row=7,sticky=tk.N+tk.E )

choice_nature = IntVar()
checkfamous = tk.Checkbutton(app, text = "Nature ", variable = choice_nature,  
                              onvalue = 1, offvalue = 0, width = 7
                              )
checkfamous.grid(column=0,row=8,sticky=tk.N+tk.E )





end_program = tk.Button (app, text='End', bg='red', fg='white', command=close_window, width=5)
end_program.grid (column=2,row=8,sticky=tk.N+tk.W, )


save_next = tk.Button (app, text='Save & Next', command=Save_Next,bg='blue', fg='white', width=9)
save_next.grid (column=3,row=8,sticky=tk.N+tk.W,  )

view_result = tk.Button (app, text='Summary', bg='green', fg='white', command=New_Window, width=10)
view_result.grid (column=4,row=8,sticky=tk.N+tk.W )



app.mainloop()


