#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 21:32:26 2018

@author: taranraghuram
"""

def week_2():
    int_array = []
    with open("integer_array.txt") as f:
        lines = f.read().splitlines()
    
    for i in lines:
        int_array.append(int(i))
        
    print(inversion_sort(int_array))


def inversion_sort(n):
    '''
    returns a sorted list and the number of inversions made
    
    '''    
    
    result = []
    
    if len(n) == 1:
        return [n,0]
    
    #if not base case, recursively sort arrays and keep track of inversions
    
    n1 = inversion_sort(n[:len(n)//2])
    n2 = inversion_sort(n[len(n)//2:])
        
    i = 0
    j = 0
    inversions = 0
    
    while i < len(n1[0]) and j < len(n2[0]):
        if n1[0][i] > n2[0][j]:
            result.append(n2[0][j])
            inversions += len(n1[0])-i
            j += 1
        else:
            result.append(n1[0][i])
            i += 1
    result += n1[0][i:]
    result += n2[0][j:]
    inversions = inversions + n1[1] + n2[1]
    
    return [result, inversions]
    

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
