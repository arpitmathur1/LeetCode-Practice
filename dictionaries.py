# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 09:57:35 2021

@author: arpit
"""

data = {}
data['a'] = [(1,'a'),(2,'b'),(3,'c'),(4,'d')]
data['b'] = [(1,'q'),(2,'w'),(3,'e'),(4,'r'), (5,'t')]


new_data = {}

for dat in data.keys():
    for element in data[dat]:
        if element[0] in new_data.keys():
            new_data[element[0]].append( [dat, element[1]] )
        else:
            new_data[element[0]] = [ [dat, element[1]] ]


print(new_data)