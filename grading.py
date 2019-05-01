# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:16:20 2019

@author: henry
"""


sum = 0
list1=[]      #important to first initialize list or it can't tell.
for i in range(5):
     list1.append(int(input("please enter a number between 0 to 20: ")))
     sum += list1[i]

print("the enter numbers are ", list1)
print("the total is ", sum)

if sum > 85 :
     grade= "A"
elif sum > 75 :
     grade= "B"
elif sum > 65 :
     grade= "C"
elif sum > 50 :
     grade= "D"
else:
     grade= "F"

print ("grade is ", grade)