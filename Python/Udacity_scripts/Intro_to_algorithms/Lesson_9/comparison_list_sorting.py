# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 17:47:44 2019

@author: roush

Sort a list by using the comparison model
BigO (or BigTheta) == n*log(n)??
"""

import random

testlist = [4,1,55,1,311,556,2,33,44,109,592958,5293,50]

def sort_list(a_list):
    for fillslot in range(len(a_list)): # iterate through positions in list
        position_of_min = fillslot # minimum value could be that in the fillslot
        for position in range(fillslot,len(a_list)): # iterate from fillslot to end of list
            if a_list[position] < a_list[position_of_min]:
                position_of_min = position
        intermediate = a_list[fillslot] # place to store current fillslot value, since it's about to replaced
        a_list[fillslot] = a_list[position_of_min]
        a_list[position_of_min] = intermediate # swap position of original min value with fillslot value
    return a_list

print(sort_list(testlist))