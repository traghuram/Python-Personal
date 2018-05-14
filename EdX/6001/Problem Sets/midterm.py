# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 17:51:26 2017

@author: traghuram
"""

# new class

def sumDigits(N):
    if len(str(N)) == 1:
        return N
    
    else:
        return sumDigits(N//10) + (N % 10)


def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here  
    
    container = []
    
    for i in aDict.keys():
        if aDict[i] == target:
            container.append(i)
    
    container.sort()
    return container


def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    L.reverse()
    
    for i in L:
        i.reverse()

#old
def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    
    ''' - recursive form (doesn't work above k = 1000, exceeds recursion depth)
    triangleList = [1]
    
    def triangles(s = k):
        if s == 1:
           return 1
        
        return triangles(s-1) + s
    
    for i in range(k):
        triangleList.append(triangles(i+1))
    '''
    
    triangleList = [] # closed form
    
    for i in range(k):
        triangleList.append((i+1)*(i+2)/2)

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
    
    # optional lambda version
    # return lambda x: sum(e*x**n for n, e in enumerate(reversed(L)))
    
    return inner


def is_list_permutation(L1,L2):
    
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    
    # Your code here
    if len(L1) != len(L2):
        return False
    
    if L1 == [] and L2 == []:
        return (None, None, None)
    
    modeElement = ()
    
    while L1 != [] and L2 != []:
        if L1[0] in L2:
            tupleElement = (L1[0],)
            modeElement = modeElement + tupleElement
            L2.remove(L1[0])
            del L1[0]
            
        else:
            return False
    
    largestElement = ()

    for n in modeElement:
        if largestElement == ():
            largestElement = (n, modeElement.count(n), type(n))
        else:
            if modeElement.count(n) > largestElement[1]:
                largestElement = (n, modeElement.count(n), type(n)) # no longer points to old tuple, that gets garbage collected
    
    return largestElement
    
    
