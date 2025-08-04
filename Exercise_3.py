# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:43:57 2020

@author: Lenovo
"""
import random

friends_name = ['Jimmy', 'Pig', "Muffy", "Sam", "Tom", "Pandi", "Parisa", "Cutie", "PigPig"]
stored_items = len(friends_name)


# Exercise 3.1 using a for loop
for friends in friends_name:
    print (friends.lower())


#Exercise 3.1 using a While loop
counter=0
friends_count=1
while counter < stored_items:
   print ( "My" , friends_count, "st friend name is:\t ", {friends_name[counter].upper()} )
   friends_count +=1
   counter +=1
   
   
# Exercise 3.2 using a  for loop (its so much easier)

for friends in friends_name:
    print (" Hello ", friends.title(), "how are you doing today ?")  
    if friends == "Tom":
         print (" Y'all right ", friends.title(), "how are you doing today ?")
   
    

 # Exercise 3.4

vehicle_name =  ['tesla', 'BMW', 'mercedez', 'Honda', 'Toyota', 'Perodua', 'Proton','volvo','audi']
random_syntax = [ 'great vehicle', 'waste of money', 'best of breed', 'lancau car']

vehicle_name[0] = 'saab'
vehicle_name.insert (0, 'tesla')
new_additions = [ 'Daihatsu', 'Posrche', 'Ferari','Lexus', "Mistubishi", 'KIA', 'Kancil']
    
for added_vehicles in new_additions:
      vehicle_name.append(added_vehicles)    

for vehicles in vehicle_name:
    generated_text = random_syntax[random.randrange(0,len(random_syntax))]
    print (vehicles.title(), "is a", generated_text.title())
       
    # Exercise 3.5

vehicle_name =  ['tesla', 'BMW', 'mercedez', 'Honda', 'Toyota', 'Perodua', 'Proton','volvo','audi']
random_syntax = [ 'great vehicle', 'waste of money', 'best of breed', 'lancau car']

vehicle_name[0] = 'saab'
vehicle_name.insert (0, 'tesla')
new_additions = [ 'Daihatsu', 'Posrche', 'Ferari','Lexus', "Mistubishi", 'KIA', 'Kancil']


for added_vehicles in new_additions:
      vehicle_name.append(added_vehicles)    
del vehicle_name[2]

for vehicles in vehicle_name:
    generated_text = random_syntax[random.randrange(0,len(random_syntax))]
    print (vehicles.title(), "is a", generated_text.title())
       