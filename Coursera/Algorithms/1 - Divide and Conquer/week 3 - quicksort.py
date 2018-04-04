# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 18:41:01 2018

@author: traghuram
"""

#quicksort - l is starting position, r is end position. For first elem pivot

def quicksort_first(A, l=0, r=0):
        
    if r==l:
        print("At the end!")
    
    else:
        p = A[l]
        i = l+1
                
        for j in range(l+1, r):
            if A[j] < p:
                A[i], A[j] = A[j], A[i]
                i += 1
                print(A)
        
        A[l], A[i-1] = A[i-1], A[l]
        print(A)
        
        quicksort_first(A,0,i-2)
        quicksort_first(A,i,len(A))
        
        print(A)
    