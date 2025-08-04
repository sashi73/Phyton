# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:50:52 2020

@author: Lenovo
"""

import os
import colorama
from colorama import Fore, Style

#clear the console before you print the output
clear = lambda : os.system('cls')
clear()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#Function to sort by the year
def sort_by_year(result):
        return result['year']


#Function to sort by the country
def sort_by_country(result):
    return result['country']
#Fuction to sort by country in reverse order
def sort_by_country_reverse(result):
    return sorted(result['country'],reverse=True)

# To check on what it is known for
def known_for(result):
      if dives == 'diving' :
           Diving_Hot_list.append(country['country'].title())
      elif dives == 'shopping' :
           Shopping_Paradise.append(country['country'].title())
      elif dives == 'food' :
           Food_Heaven.append(country['country'].title())
      elif dives == 'temple' :
           Temple.append(country['country'].title())
      return()  

#function to delete the first index
def delete_first_index(key):
    del key[0]
    return()

def recommendation(caption,zone,attraction):
    Scuba_Zones = ''
    caption.title()
    print("\n")
    for dive_zones in zone:
        Scuba_Zones = Scuba_Zones + dive_zones + ","
    if attraction=='diving':    
        print  (Fore.YELLOW + caption.lstrip(), color.END,Scuba_Zones)
    elif attraction=='shopping':
        print  (Fore.GREEN + caption.lstrip(), color.END,Scuba_Zones)
    elif attraction=='food':
        print  (Fore.CYAN + caption.lstrip(), color.END,Scuba_Zones)
    elif attraction=='temple':
        print  (Fore.MAGENTA+ caption.lstrip(), color.END,Scuba_Zones)
    return()
    
#List of countries that I have visited in South East Asia by year
countries_visited_Sea = [
    {'country':'malaysia','year' : 1973, 'known for' : 'diving, food'},
    {'country' :'singapore','year' : 1999, 'known for' : 'events, shopping'},
    {'country' :'indonesia', 'year' : 2004, 'known for' : 'nature,  diving'},
    {'country' :'brunei', 'year' : 2020, 'known for' : 'nothing'},
    {'country' :'thailand', 'year' : 1999, 'known for' : 'fun, lesiure, food,diving,temple'},
    {'country' :'cambodia', 'year' : 2008, 'known for' : 'temple, relics'},
    {'country' :'vietnam', 'year' : 2008, 'known for' : 'nature, food'}
  ]


Countries_Sorted=['']
Desc_Order=['']
Diving_Hot_list=['']
Shopping_Paradise=['']
Food_Heaven = ['']
Temple=['']


# input a new country into the list
country_name = input("Please enter the name of the country:")
year_visited = int(input("Please enter the year you first visted the country:"))
why_famous = input ("Please enter what is it famous for followed by a comma:") 
#convert to lower case
country_name = country_name.lower()
why_famous= why_famous.lower()

# append a new country to the list
countries_visited_Sea.append( {'country' :country_name, 'year' : year_visited, 'known for': why_famous}, ) 


# print the list as it is before sorting
print (countries_visited_Sea)

input("Press to Continue: ")

#calling function to sort by year
countries_visited_Sea.sort(key=sort_by_year)

#Defining first and last position in the list
first_object = 0
last_object = len(countries_visited_Sea)
counter_position = 0


#Sorting by Year
for country in countries_visited_Sea:
    #sorted (country)
    
        if counter_position == 0:
            print ("The very first country you visited in South East Asia is" ,country['country'].title(), "in the year", country['year'], )
        elif  counter_position < last_object-1 :
            print ("The next country you visited in South East Asia is" ,country['country'].title(), "in the year", country['year'] )
        
        if counter_position== last_object:
            print ("The last country you visited in South East Asia is" ,country['country'].title(), "in the year", country['year'] )
        counter_position= counter_position + 1
print ("The last country you visited in South East Asia is" ,country['country'].title(), "in the year", country['year'] , "\n")


#Sorting by Country name Asc
countries_visited_Sea.sort(key=sort_by_country)
for country in countries_visited_Sea:
    print (country['country'].title())
    
    # move it to a new list just by country name
    Countries_Sorted.append( country['country'])
print ("\n")   


# move it to a new by country name in a reverse order
Desc_Order = sorted(Countries_Sorted,reverse=True)
#remove the last item in the list
Desc_Order.pop()


#Sorting by name desc 


for country in Desc_Order:
    print(country.title())
   
print ("\n")  


# print what the countries are famous_for
for country in countries_visited_Sea:
    print (country['country'].title(), 'is famous for' , country['known for'].title())
    Diving_Spot = country['known for'].split(",")
    for dives in Diving_Spot:
        dives = dives.strip()
        known_for(dives)
        


#function the delete the first index position in a list
delete_first_index(Diving_Hot_list)
delete_first_index(Shopping_Paradise)
delete_first_index(Food_Heaven)
delete_first_index(Temple)
print(Temple)

recommendation('The best countries for Scuba Diving in ASEAN:',Diving_Hot_list,'diving')
recommendation('The shopping paradise in ASEAN:',Shopping_Paradise,'shopping')
recommendation('The food heaven in ASEAN:',Food_Heaven,'food')
recommendation('Best place in Asean for Temples',Temple,'temple')