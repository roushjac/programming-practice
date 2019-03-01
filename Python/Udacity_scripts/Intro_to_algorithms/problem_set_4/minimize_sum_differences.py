# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:39:41 2019

@author: roush
"""
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
# 
# Your code should run in Theta(n) time
#
import random

testlist = [4,1,2,5,22,5,256,36,8,9,36,888]

def minimize_absolute(L):
    '''
    The value that minimizes the sum of absolute differences between itself
    and all elements of L is the median of list L.
    Since any sorting algorithm takes at least Theta(n*logk) or (n*logn),
    we will not use a full sorting algorithm.
    This is basically a top-K problem where we want the top (len(L)/2)
    '''
    if len(L) % 2 == 0: # if length of list is even, average two middle values for median
        right_middle = find_top_K(L, (len(L)//2)+1)[-1]
        left_middle = find_top_K(L, len(L)//2)[-1]
        return (right_middle + left_middle) / 2
    # only other valid condition is if length of list is odd - just pick middle value
    return find_top_K(L, (len(L)//2)+1)[-1]
    
def find_top_K(L, k):
    # finds top K elements of list L (top meaning smallest in this case)
    # Pick random element of L as pivot point
    pivot_element = L[random.randint(0,len(L)-1)]
    smaller = [x for x in L if x < pivot_element]
    bigger = [x for x in L if x > pivot_element]
    same_as_pivot = [x for x in L if x == pivot_element]
    if len(smaller) == k: return smaller # top K elements of the original list, unsorted
    if len(smaller)+len(same_as_pivot) == k: return smaller + same_as_pivot
    if len(smaller) > k: return find_top_K(smaller, k) # recurse if "smaller than" list includes too many elements
    if len(smaller) < k and len(smaller)+len(same_as_pivot) > k:
        # k is in the middle of the list of pivot points after they are added on to smaller
        return smaller+same_as_pivot[:(k-len(smaller))]
    # if smaller list is only part of top K, recurse on bigger list and add on smaller list + pivot points
    if len(smaller) < k: return smaller + same_as_pivot + find_top_K(bigger, k-len(smaller)-len(same_as_pivot))
    
print(minimize_absolute(testlist))
