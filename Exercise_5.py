# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 00:40:23 2020

@author: Lenovo
"""
import random
import os

clear = lambda : os.system('cls')
clear()

 # Exercise 3.5

vehicle_name =  ['tesla', 'BMW', 'mercedez', 'honda', 'toyota', 'perodua', 'proton','volvo','audi']
random_syntax = [ 'great vehicle', 'waste of money', 'best of breed', 'lancau car']

vehicle_name[0] = 'saab'
vehicle_name.insert (0, 'tesla')
new_additions = [ 'daihatsu', 'posrche', 'ferari','lexus', "mistubishi", 'kIA', 'kancil']


for added_vehicles in new_additions:
      vehicle_name.append(added_vehicles)    
del vehicle_name[2]

for vehicles in vehicle_name:
    generated_text = random_syntax[random.randrange(0,len(random_syntax))]
    print (vehicles.title(), "is a", generated_text.title(), '/n')
       
print ("\n", vehicle_name.pop(), "\n")

vehicle_name.reverse()
print( sorted(vehicle_name), "\n")

for vehicles in vehicle_name:
    generated_text = random_syntax[random.randrange(0,len(random_syntax))]
    print (vehicles.title(), "is a", generated_text.title())