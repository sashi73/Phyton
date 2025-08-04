# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:08:15 2020

@author: Lenovo
"""


name= " This is a simple test "

Stripped_Name = name.strip()
Length = len (Stripped_Name)

#Count = name.count(name)
#print (Count)
print (Stripped_Name.title())
print (Stripped_Name.upper())
print (Stripped_Name.lower())
number_of_letters = len (Stripped_Name) - Stripped_Name.count(" ")
print ("Total Length: ", Length)
print( "Number of Letters" , number_of_letters)
Total_of_white_space =  Length - number_of_letters
print ("White Space: ", Total_of_white_space)
#print(' White Space: ", name.format())