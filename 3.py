# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:59:45 2021

@author: arpit
"""

def good_substring(string):
    string = string.split('')
    print(string)
    print(len(string))
    if len(string) == len(set(string)):
        return True
    else:
        return False

print(good_substring("abca"))