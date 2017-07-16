# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 17:51:26 2017

@author: traghuram
"""

def is_triangular(k):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    
    triangleList = [1]
    
    def triangles(s = k):
        if s == 1:
           return 1
        
        return triangles(s-1) + s
    
    for i in range(k):
        triangleList.append(triangles(i+1))

    if k in triangleList:
        return True
    
    return False


def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    
    vowels = 'AaEeIiOoUu'
    voweless = ''
    
    for char in s:
        if char not in vowels:
            voweless = voweless + char

    print (voweless)
        
    
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    
    LUnique = set(L)
    
    largestOdd = None
    
    for n in LUnique:
        
        counter = 0
        
        for i in L:
            if i == n:
                counter += 1
                
        if counter % 2 == 1:
            if largestOdd != None:
                if n > largestOdd:
                    largestOdd = n
            else:
                largestOdd = n
    
    return largestOdd
            

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    
    dictValues = set(d.values())
    inverseDict = {}
    
    for x in dictValues:
        
        dictKeys = []
        for y in d.keys():
            if d[y] == x:
                dictKeys.append(y)
        
        dictKeys.sort()
                           
        inverseDict[x] = dictKeys
    
    return inverseDict


def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    def inner(x):
        summing = 0
        
        for n in range(len(L)):
            summing = summing + L[n]*x**(len(L)-(n+1))
            
        return summing
    
    return inner


def is_list_permutation(L1,L2):
    
    

