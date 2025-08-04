# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:21:30 2020

@author: Lenovo
"""
import random
import os

#clear the console before you print the output
clear = lambda : os.system('cls')
clear()

#List of countries that I have visited in South East Asia. Created Two more empty list to store 
# the results in Asc and Desc
countries_visited_Sea = ['malaysia', 'singapore', 'indonesia','brunei', 'thailand','cambodia', 'vietnam']
sorted_countries =['']
desc_order=['']
reverse_order=['']


# sorting in ascending order and printing in the country name in such order
sorted_countries = sorted(countries_visited_Sea)

for country in sorted_countries:
    sorted (country)
    print (country.title())
print ("\n")

# sorting in descending order and printing in the country name in such order
desc_order = sorted(countries_visited_Sea,reverse=True)

for country in desc_order:
    print (country.title())
print ("\n")

# sorting in reverese order and printing in the country name in such order
reverse_order = reversed(countries_visited_Sea)

for country in reverse_order:
    print (country.title())
print ("\n")