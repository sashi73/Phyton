# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:50:52 2020

@author: Lenovo
"""

import random
import os


#clear the console before you print the output
clear = lambda : os.system('cls')
clear()


#Function to sort by the year
def sort_by_year(result):
    return result['year']


#Function to sort by the country
def sort_by_country(result):
    return result['country']

def sort_by_country_reverse(result):
    return sorted(result['country'],reverse=True)

#List of countries that I have visited in South East Asia by year
countries_visited_Sea = [
    {'country':'malaysia','year' : 1973},
    {'country' :'singapore','year' : 1999},
    {'country' :'indonesia', 'year' : 2004},
    {'country' :'brunei', 'year' : 2020},
    {'country' :'thailand', 'year' : 1999},
    {'country' :'cambodia', 'year' : 2008},
    {'country' :'vietnam', 'year' : 2008}
  ]


Countries_Sorted=['']
Desc_Order=['']

# append a new countery to the list
countries_visited_Sea.append( {'country' :'phillipines', 'year' : 2014}) 


# print the list as it is before sorting
print (countries_visited_Sea)

input("Press to Continue: ")

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


    