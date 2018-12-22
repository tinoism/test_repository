#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 09:21:44 2018

@author: Christinoism

Version:
1) regular binary search
2) bs in nearly sorted array: each element displaced by at most one from the correct sorted:
    ex. B =  [2, 1, 3, 5, 4, 7, 6, 8, 9]. Conduct BS in log(n)

    
"""

def binary_search_iter(A, n, x):
    A = sorted(A)
    lo = 0
    hi = n -1
#    if lo == hi:                       # don't need to check this because
#        return 
#    mid = (hi-1) / 2                   # don't need to calculate mid before loop

    while lo <= hi:
        mid = (lo + hi) / 2             # this will be the lower rounded bound
        
        # first condition check
        
        if A[mid] == x:
            return mid
        
        if x > A[mid]:
            lo = mid + 1
        
        if x < A[mid]:
            hi = mid - 1
    
    return -1

def binary_search_rec(A, x, lo, hi):
    
    if lo <= hi:                        # important! don't forget to check! 
        mid = (lo + hi) / 2             
        mid_elem = A[mid] 
        if mid_elem == x:
            return mid
        
        if x > mid_elem:
            lo = mid + 1
            return binary_search_rec(A, x, lo, hi)      # return the recursive call result! 
        
        else: 
            hi = mid - 1
            return binary_search_rec(A, x, lo, hi)
    return -1



def nearly_sorted_bs(A, n, x):
    lo = 0
    hi = n -1
    while lo <= hi:
        mid = (lo + hi)/2
        if A[mid] == x:
            return mid
        
        if mid - 1 >= 0 and A[mid - 1] ==x:
            return mid - 1
        
        if mid + 1 <= n -1 and A[mid + 1] ==x:
            return mid + 1
        
        if A[mid] < x:
            lo = mid + 2
        
        else:
            hi = mid - 2
    return -1
    
    
    
    
if __name__ == "__main__":
    A = [ 2 ,3 , 9 , 12, 15]
    
    B =  [2, 1, 3, 5, 4, 7, 6, 8, 9]
    
    
    print binary_search_iter(A, 5, 12)
    print binary_search_iter(A, 5, -3)
    
    print nearly_sorted_bs(B, 10, 5)
    print nearly_sorted_bs(B, 10, 2)
    print nearly_sorted_bs(B, 5, 3)
    
    print binary_search_rec(A, 12, 0, 4)