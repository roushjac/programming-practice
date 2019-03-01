# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:46:12 2019

@author: roush
"""

#
# Given a list L of n numbers, find the mode 
# (the number that appears the most times).  
# Your algorithm should run in Theta(n).
# If there are ties - just pick one value to return 
#

def mode(L):
    mode_counter = {}
    current_max = L[0]
    for number in L: # populate dictionary with counts of each number
        print(mode_counter)
        if number not in mode_counter:
            mode_counter[number] = 1
            continue
        else:
            mode_counter[number] += 1
        if mode_counter[number] > mode_counter[current_max]:
            current_max = number
    return current_max
    
    
print(mode([1,1,3,3,3,4,5,6]))
    
    
####
# Test
#
import time
from random import randint

def test():
    assert 5 == mode([1, 5, 2, 5, 3, 5])
    iterations = (10, 20, 30, 100, 200, 300, 1000, 5000, 10000, 20000, 30000)
    times = []
    for i in iterations:
        L = []
        for j in range(i):
            L.append(randint(1, 10))
        start = time.clock()
        for j in range(500):
            mode(L)
        end = time.clock()
        print (start, end)
        times.append(float(end - start))
    slopes = []
    for (x1, x2), (y1, y2) in zip(zip(iterations[:-1], iterations[1:]), zip(times[:-1], times[1:])):
        print ((x1, x2), (y1, y2))
        slopes.append((y2 - y1) / (x2 - x1))
    # if mode runs in linear time, 
    # these factors should be close (kind of)
    print(slopes)

test()