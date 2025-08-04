# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:21:11 2020

@author: Lenovo
"""
# Exercise 1: Python Crash Course 2nd Edition

Name = "Sashi kumar Sivam"

#Assignment 1
print ("Hello," , Name.strip() , ",would like to learn some Python today? \n")

#Assignment 2
print(Name.lower())
print (Name.upper())
print (Name.title(),"\n")

#Assignment 3
print ("Albert Einstein once said, “'A person who never made a mistake never tried anything new'.\n")
Famous_Person= " Albert Einstein"
Famous_Quote = "'A person who never made a mistake never tried anything new'"
print (Famous_Person.lstrip(), Famous_Quote, "\n")

#Assignment 4
Long_Name = "\t Sashi \t Kumar \t Sivam \t"
print (Long_Name)
print (Long_Name.lstrip())
print( Long_Name.rstrip())
print( Long_Name.strip())