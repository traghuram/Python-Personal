#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 21:32:26 2018

@author: taranraghuram
"""


def count_inversions(n):
    '''
    returns a sorted list and the number of inversions required
    
    '''    


def mergesort(n):
    '''
    if n is empty:
        return error message
    
    if base case (array size is 2 or less):
        if array size is 2:
            compare first and second element, swap for size    
        
        return array (pass array back up)
    
    if not base case:
        recursive mergesort call, pass down first half of input
        recurvsive mergesort call, pass down second half of input
        merge
        
    '''
    
    result = []

    
    if n == []:
        print("Insert an array. Dumbass.")
    
    elif len(n)<=1:
        
        return n
    
    else:
        #print(n)
        n1 = mergesort(n[:len(n)//2])
        n2 = mergesort(n[len(n)//2:])
        
        i = 0
        j = 0
        
        while i < len(n1) and j < len(n2):
            if n1[i] > n2[j]:
                result.append(n2[j])
                j += 1
            else:
                result.append(n1[i])
                i += 1
        result += n1[i:]
        result += n2[j:]
        return result
