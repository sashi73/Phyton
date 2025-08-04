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



global summary_window

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
             'Vietnam']

year_visited =['']

countries_visited_Sea = [
    {'country':'','year' : 1973, 'known for' : ''},
     ]


Countries_Sorted=['']
Desc_Order=['']
Diving_Hot_list=['']
Shopping_Paradise=['']
Food_Heaven = ['']
Temple=['']




 
def Current_Year(current_year):
    current_year = current_year.year
    current_year = current_year + 1
    
    return(current_year)

def sort_by_year(result):
        return result['year']

#function to delete the first index
def delete_first_index(key):
    del key[0]
    return()

def recommendation(caption,zone,attraction):
    Screen_X_Position = 20
    #Defining first and last position in the list
    Call_clear()
    Scuba_Zones = ''
    caption.title()
    
    
    for dive_zones in zone:
        Scuba_Zones = Scuba_Zones + dive_zones + ","
        
    if attraction=='diving':    
        Scuba_Zones = caption + Scuba_Zones
        label_text =  tk.Label(summary_window,text =  Scuba_Zones ,width =85, anchor='w')
        label_text.place(x=1 ,y=Screen_X_Position)
        Screen_X_Position=Screen_X_Position + 10
        print  (caption.lstrip(), Scuba_Zones)
    elif attraction=='shopping':
        Scuba_Zones = caption + Scuba_Zones
        label_text =  tk.Label(summary_window,text =  Scuba_Zones ,width =85, anchor='w')
        label_text.place(x=Screen_X_Position ,y=Screen_X_Position)
        Screen_X_Position=Screen_X_Position + 10
        print  (caption.lstrip(), Scuba_Zones)
    elif attraction=='food':
        Scuba_Zones = caption + Scuba_Zones
        label_text =  tk.Label(summary_window,text =  Scuba_Zones ,width =85, anchor='w')
        label_text.place(x=Screen_X_Position ,y=Screen_X_Position)
        Screen_X_Position=Screen_X_Position + 10
        print  ( caption.lstrip(), Scuba_Zones)
    elif attraction=='temple':
        Scuba_Zones = caption + Scuba_Zones
        label_text =  tk.Label(summary_window,text =  Scuba_Zones ,width =85, anchor='w')
        label_text.place(x=Screen_X_Position ,y=Screen_X_Position)
        Screen_X_Position=Screen_X_Position + 10
        print  (caption.lstrip(), Scuba_Zones)
      
    return()


# To check on what it is known for
'''
def known_for(result):
      if result == 'diving' :
           Diving_Hot_list.append(country['country'].title())
      elif result == 'shopping' :
           Shopping_Paradise.append(country['country'].title())
      elif result == 'food' :
           Food_Heaven.append(country['country'].title())
      elif result == 'temple' :
           Temple.append(country['country'].title())
      return()  
'''

#quit the program
def close_window (): 
    app.destroy()
   

#check results
def Save_Next(): 
    known_for =''
    
    if choice_diving.get() == 1:
       known_for = known_for + 'diving,' 
    if choice_leisure.get() == 1:
        known_for = known_for + 'leisure,'        
    if choice_food.get() == 1:
       known_for = known_for + 'food,'  
    if choice_shopping.get() == 1:
       known_for = known_for + 'shopping,'  
    if choice_temples.get() == 1:
       known_for = known_for + 'temples,' 
    if choice_beach.get() == 1:
       known_for = known_for + 'sandy beach,' 
    if choice_liquor.get() == 1:
       known_for = known_for + 'liquor,'  
    if choice_nature.get() == 1:
       known_for = known_for + 'nature,'  
    
    countries_visited_Sea.append( {'country' :comboCountry.get() , 'year' : comboYear.get(),
                                   'known for':known_for}) 
 
    print (countries_visited_Sea)   
    Clear_New()
  

def Sort_by_year():
    countries_visited_Sea.sort(key=sort_by_year)
    Screen_Y_Position = 5
    #Defining first and last position in the list
    Call_clear()
    last_object = len(countries_visited_Sea)-1
    Last_Visit = 0
    First_Visit = 0
    Total_Visit = 0
    Visit_Summary ='Looks like you have been visiting South East Asia for '    
    counter_position = 0
    Country_Visited_Sequence = ''
    for country in countries_visited_Sea:
            #sorted (country)
    
         if counter_position == 0:
             Country_Visited_Sequence =  ('The very first country you visited in South East Asia is ' + country['country'].title() + ' in the year ' + country['year']  )
             label_text =  tk.Label(summary_window,text = Country_Visited_Sequence,width =85, anchor='w')
             label_text.place(x= 5 ,y=Screen_Y_Position)
             First_Visit = int(country['year'])
            
          
         elif  0 < counter_position < last_object:
              Country_Visited_Sequence =('The next country you visited in South East Asia is ' + country['country'].title() + ' in the year '+ country['year'])
              label_text =  tk.Label(summary_window,text = Country_Visited_Sequence,width =85, anchor='w')
              Screen_Y_Position = Screen_Y_Position + 30
              label_text.place(x= 5,y= Screen_Y_Position )
           
         if counter_position== last_object:
              Country_Visited_Sequence = ('The last country you visited in South East Asia is ' + country['country'].title() + ' in the year '+ country['year'] )
              label_text =  tk.Label(summary_window,text = Country_Visited_Sequence,width =85, anchor='w')
              Screen_Y_Position = Screen_Y_Position + 30
              label_text.place(x= 5 ,y= Screen_Y_Position )
              Last_Visit = int(country['year'])
         counter_position= counter_position + 1 
            
    Total_Visit =  Last_Visit - First_Visit
          
    Visit_Summary = (Visit_Summary + ' ' + str(Total_Visit) + ' Years!')
   
    label_text =  tk.Label(summary_window,text = Visit_Summary,width =85, anchor='w')
    Screen_Y_Position = Screen_Y_Position + 30
    label_text.place(x= 5 ,y= Screen_Y_Position )
    
def Recommendations_Sorting():
    global dives
    
    for country in countries_visited_Sea:
        print (country['country'].title(), 'is famous for' , country['known for'].title())
        Diving_Spot = country['known for'].split(",")
        for dives in Diving_Spot:
            dives = dives.strip()
            #known_for(dives)
            if dives == 'diving' :
                Diving_Hot_list.append(country['country'].title())
            elif dives == 'shopping' :
               Shopping_Paradise.append(country['country'].title())
            elif dives == 'food' :
               Food_Heaven.append(country['country'].title())
            elif dives == 'temple' :
               Temple.append(country['country'].title())
        


    #function the delete the first index position in a list
    delete_first_index(Diving_Hot_list)
    delete_first_index(Shopping_Paradise)
    delete_first_index(Food_Heaven)
    delete_first_index(Temple)
   
    
    if len(Diving_Hot_list) > 0:
        recommendation('The best countries for Scuba Diving in ASEAN:',Diving_Hot_list,'diving')
    if len(Shopping_Paradise) > 0:
        recommendation('The shopping paradise in ASEAN:',Shopping_Paradise,'shopping')
    if len(Food_Heaven) > 0:
        recommendation('The food heaven in ASEAN:',Food_Heaven,'food')
    if len(Temple) > 0:
        recommendation('Best place in Asean for Temples',Temple,'temple')
       
       
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


def Call_print():
      
      label_text =  tk.Label(summary_window,
                    text = "The following is the list of countries you visited in Asean",width =55,
                    anchor='w')
      label_text.place(x=0,y=5)
      
      
def Call_clear():
     global label_text
     label_text =  tk.Label(summary_window,text = "                                         ",width =85,
                    anchor='w')
     
     y_position = 0
     for position in range(300): 
       
        label_text.place(x=1,y=position)
        y_position = y_position + 1
        
    
def New_Window():
      global summary_window
      summary_window = tk.Toplevel(app) 
      summary_window.geometry('480x400')
      summary_window.title('My Asean Travel Buddy - Summary')
      summary_window.resizable(0,0)
      
     
      button_summ = tk.Button (summary_window, text='End', bg='red',
                                fg='white', command= summary_window.protocol("WM_DELETE_WINDOW"), width='10')
      button_summ.place(x=350,y=350)
      
      button_clear = tk.Button (summary_window, text='Sort By Year', bg='white',
                                fg='black', command= Sort_by_year, width='12')
      button_clear.place(x=250,y=350)
      button_clear = tk.Button (summary_window, text='Recommendation', bg='grey',
                                fg='black', command= Recommendations_Sorting, width='15')
      button_clear.place(x=140,y=350)
      
      Call_print()
      
      
      
      
     
      
 # clear first item in the list
countries_visited_Sea.pop()     
    
# initiazlizing tkinter framework for GUI
app = tk.Tk()

# window size W * H
app.geometry('480x180')
# Window title
app.title('My Asean Travel Buddy')
app.resizable(0,0)
next_year = Current_Year(datetime.datetime.now())

#new tople level window


year = range(1920,next_year)
for yearenumator in year: 
    year_visited.append(yearenumator)

year_visited.pop(0)

year_visited.sort(reverse=True)


labelCountry = tk.Label(app,
                    text = "Which Country did you visit:",width =25,
                    anchor='w')


   
    
labelCountry.grid(column=0, row=0)

sorted(countries)
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


