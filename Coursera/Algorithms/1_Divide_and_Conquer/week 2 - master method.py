#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 21:32:26 2018

@author: taranraghuram
"""

import numpy as np
import time

def week_2(n = 2**7):
    int_array = []
    with open("integer_array.txt") as f:
        lines = f.read().splitlines()
    
    for i in lines:
        int_array.append(int(i))
        
    print("Number of inversions:", inversion_sort(int_array)[1])
    
    x = np.arange(0,n**2).reshape(n,n)
    y = np.arange(0,n**2).reshape(n,n)
    
    start = time.time()
    matrix_mult(x,y)
    end = time.time()
    print("Brute force matrix multiplication:", end - start)
    
    start = time.time()
    matrix_recur(x,y)
    end = time.time()
    print("Recursive matrix multiplication:", end - start)
    
    start = time.time()
    matrix_strassen(x,y)
    end = time.time()
    print("Strassen matrix multiplication:", end - start)

    


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


def matrix_mult(x = [[1,2],[3,4]], y = [[5,6],[7,8]]):
    '''
    Defines normal matrix multiplication, O(n^3) time for two eligible matrices
    
    If matrices cannot be multiplied, calls you on your BS
    '''
    
    x_rows = len(x)
    x_cols = len(x[0])
    
    y_rows = len(y)
    y_cols = len(y[0])
    
    if x_cols != y_rows:
        stop = "Stop dumbass - fix your matrices, the columns in x need to match rows in y"
        return stop
    
    result = []
    for i in range(x_rows):
        result.append([])
        
        for j in range(y_cols):
            sumproduct = 0
            
            for k in range(x_cols):
                sumproduct += x[i][k]*y[k][j]
            
            result[i].append(sumproduct)
    
    return result
    
    

def matrix_recur(x = np.arange(1,5).reshape(2,2), y = np.arange(5,9).reshape(2,2)):
    '''
    Defines recursive matrix multiplication, still O(n^3) time
    
    If matrices cannot be multiplied, calls you on your BS
    '''
    
    x_rows = x.shape[0]
    x_cols = x.shape[1]
    
    y_rows = y.shape[0]
    y_cols = y.shape[1]  
    
    if x_cols != y_rows:
        stop = "Stop dumbass - fix your matrices, the columns in x need to match rows in y"
        return stop
    
    if x.size < 16 or y.size < 16 or y_cols == 1 or x_rows == 1:
        return np.dot(x,y)
    
    # if not using numpy, then need for loop to get n/2 elements for n/2 rows
        
    A = x[:(x_rows//2),:(x_cols//2)]
    B = x[:(x_rows//2),(x_cols//2):]
    C = x[(x_rows//2):,:(x_cols//2)]
    D = x[(x_rows//2):,(x_cols//2):]
    
    E = y[:(y_rows//2),:(y_cols//2)]
    F = y[:(y_rows//2),(y_cols//2):]
    G = y[(y_rows//2):,:(y_cols//2)]
    H = y[(y_rows//2):,(y_cols//2):]
    
    AE = matrix_recur(A,E)
    BG = matrix_recur(B,G)
    AF = matrix_recur(A,F)
    BH = matrix_recur(B,H)
    CE = matrix_recur(C,E)
    DG = matrix_recur(D,G)
    CF = matrix_recur(C,F)
    DH = matrix_recur(D,H)
    
    array1 = np.append(AE+BG, CE+DG, axis = 0)
    array2 = np.append(AF+BH, CF+DH, axis = 0)
    array = np.append(array1, array2, axis = 1)
    
    return array


def matrix_strassen(x,y):
    '''
    Defines Strassen matrix multiplication, O(<n^3) time :o
    
    If matrices cannot be multiplied, calls you on your BS
    '''

    x_rows = x.shape[0]
    x_cols = x.shape[1]
    
    y_rows = y.shape[0]
    y_cols = y.shape[1]  
    
    if x_cols != y_rows:
        stop = "Stop dumbass - fix your matrices, the columns in x need to match rows in y"
        return stop
    
    if x.size < 16 or y.size < 16 or y_cols == 1 or x_rows == 1:
        return np.dot(x,y)
            
    A = x[:(x_rows//2),:(x_cols//2)]
    B = x[:(x_rows//2),(x_cols//2):]
    C = x[(x_rows//2):,:(x_cols//2)]
    D = x[(x_rows//2):,(x_cols//2):]
    
    E = y[:(y_rows//2),:(y_cols//2)]
    F = y[:(y_rows//2),(y_cols//2):]
    G = y[(y_rows//2):,:(y_cols//2)]
    H = y[(y_rows//2):,(y_cols//2):]
    
    P1 = matrix_strassen(A,F-H)
    P2 = matrix_strassen(A+B,H)
    P3 = matrix_strassen(C+D,E)
    P4 = matrix_strassen(D,G-E)
    P5 = matrix_strassen(A+D,E+H)
    P6 = matrix_strassen(B-D,G+H)
    P7 = matrix_strassen(A-C,E+F)
    
    array1 = np.append(P5+P4-P2+P6, P3+P4, axis = 0)
    array2 = np.append(P1+P2, P1+P5-P3-P7, axis = 0)
    array = np.append(array1, array2, axis = 1)
    
    return array    