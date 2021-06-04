# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 18:41:01 2018

@author: traghuram
"""

#quicksort - l is starting position, r is end position. For first elem pivot


def load_array(file_name="problem5.6test1.txt"):
    with open(file_name,"r") as txt_file:
        test_data = [int(x) for x in txt_file.read().split()]
    return test_data


def quicksort_first(A, l=0, r=0):
    '''Sorts an array recursively
        Returns a sorted list
        Assumes some elements, no repeated elements (for now)
    '''
    
    print(A, l, r)
    
    if r==l:
        return A
    
    else:
        p = A[l]
        i = l+1
                
        for j in range(l+1, r):
            if A[j] < p:
                A[i], A[j] = A[j], A[i]
                i += 1
        
        A[l], A[i-1] = A[i-1], A[l]
                
        #if there are 1 or fewer elements to the left of the pivot, don't do left quicksort
        #elif there are no elements to the right of the pivot, do right quicksort
        #else do both

        quicksort_first(A,0,i-1)
        quicksort_first(A,i,r)
                
        return A


def quicksort(n=[], pivot=0):
    
    if len(n)==1:
        return n
    
    p = pivot
    
    #partition A around p
    
    
    # recursively sort 1st part
    # recursively sort second part
    
    return n