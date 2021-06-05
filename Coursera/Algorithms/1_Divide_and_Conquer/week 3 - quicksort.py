# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 18:41:01 2018

@author: traghuram
"""

'''
Quiz answers


Pset:
    First element comparisons = 162085
    Last element comparisons = 164123
    Median element comparisons = (should be 138,382)

'''

import numpy as np


#quicksort - l is starting position, r is end position. For first elem pivot


def load_array(file_name="problem5.6test1.txt"):
    with open(file_name,"r") as txt_file:
        test_data = [int(x) for x in txt_file.read().split()]
    return test_data


def quicksort_old(A, l=0, r=0):
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

        quicksort_old(A,0,i-1)
        quicksort_old(A,i,r)
                
        return A



test_list = [3,7,6,1,2,5]

def QuickSort(A=test_list, l=0, r=len(test_list), comparisons=0, pivot="first"):
    '''Sorts an array recursively
        Returns a sorted list
        Assumes some elements, no repeated elements (for now)
    '''
    
    if l>=r:
        #print("base case reached!")
        return A, comparisons
    
    # Choose a pivot element
    i = ChoosePivot(A, l, r, pivot)
    
    # Place chosen pivot at beginning of array
    A[l], A[i] = A[i], A[l]
    
    # Partition A around pivot and get final pivot position
    j, comparisons = Partition(A, l, r, comparisons)
    
    # recursively sort 1st and 2nd parts
    comparisons = QuickSort(A,l,j,comparisons,pivot)[1]
    # Need same comparisons var to feed into next quicksort
    comparisons = QuickSort(A,j+1,r,comparisons,pivot)[1]
    
    #print(A)
    return A, comparisons



def Partition(A,l,r,comparisons):
    '''

    Parameters
    ----------
    A : list
        input array.
    l : int
        first element of subarray.
    r : int
        last element of subarray.

    Returns
    -------
    j : int
        location of new pivot position.

    '''
    
    # Set pivot element
    p = A[l]
    i = l+1
    j = l+1
    
    # Split array into sections bigger and smaller than pivot
    while j < r:
        
        comparisons += 1
        #print(comparisons)
            
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
        
        j += 1
    
    # Place pivot in between two sections
    A[l], A[i-1] = A[i-1], A[l]
    
    return i-1, comparisons



def ChoosePivot(A,l,r,pivot="first"):
    '''

    Parameters
    ----------
    A : list
        input array.
    l : int
        first element of subarray.
    r : int
        last element of subarray.

    Returns
    -------
    int
        location of pivot element..

    '''
    if pivot == "first":
        return l
    elif pivot == "last":
        return r - 1
    elif pivot == "median":
        if (r-l)%2 == 0:
            # subtract 1
            med = np.median([A[l], A[r-1], A[(r-l)//2-1]])
            return A.index(med)
        else:
            # don't subtract 1
            med = np.median([A[l], A[r-1], A[(r-l)//2]])
            #print([A[l], A[r-1], A[len(A)//2-1]])
            #print(l, r, A.index(med))
            return A.index(med)
    else:
        return l