# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 22:25:31 2021

@author: arpit
"""

value = 333

length_of_binary_number = len(bin(value)) - 2
#print(length_of_binary_number)

current_binary = 1
number = 0
for i in range(length_of_binary_number):
    number = 2*number + current_binary
    current_binary = current_binary ^ 1

left = number
right = number >> 1

left  = value & left
right = value & right

left = left >> 1
right = right << 1

a = (right << 1) + (left >> 1)
print(a)
print(bin(a))