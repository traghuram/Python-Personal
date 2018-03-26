# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Quiz for week 1

1) nlog(n) - mergesort results in nlog(n) time for any subdivision length (will
always cancel out with the number of recursive calls)

2) True! See notebook

3) Depends on f and g - and g has to be at least as big or bigger than f, since
the ratio between 2^f and 2^g can only be bounded by a constant in certain cases.
If f gets bigger than g by varying amounts, then the proposition is not true.
If f is always bigger than g by the same factor, then that factor is c and we're good.
If g is always bigger than f, then we're good

4) For 2 arrays, 2n + c opertions = O(n)
For 3 arrays, (2n + c) + 3n + c = 5n + 2c = O(n)
For 4 arrays, (2n + c + 3n + c) + 4n + c = 9n + 3c = O(n)
For k arrays, (2n + c + 3n + c + 4n + c +... (k-1)n + c) + kn + c = (k+2)(k-1)n/2 + kc
= O(nk^2) 

5) n^2, n^2*log(n), n^log(n), 2^n, 2^(2^n)


"""



def karatsuba(n):
    
    '''
    

    '''




""" Mergesort - consists of a recursive steps that merge sorted sub-arrays of the input array.

Two versions of merge sort - first does merges by cutting array into half in each recursive call

Second version asks for the "split" amount

Both should take same amount of time since having fewer recursive calls means more merges (test this!)

"""


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
    '''
    def merge(n1, n2):
        #print(n1,n2)
        c = []
        i = 0
        j = 0
        n1_checker = True
        n2_checker = True
        
        for k in range(len(n1) + len(n2)):
            if n1[i] < n2[j] & n1_checker == True:
                c.append(n1[i])
                i += 1
                if i == len(n1):
                    i -= 1
                    n1_checker = False
            
            elif n2_checker == True:
                c.append(n2[j])
                j += 1
                if j == len(n2):
                    j -= 1
                    n2_checker = False
        #print(c)
        return c
        
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
        
    
    
    
def mergesort_k(n, k):
    '''
    k is number of subdivisions per level of mergesort

    if base case:
        blah
        
    if not base case:
        for each in k:
            recursive mergesort call, pass down 1/kth piece of input
            merge k pieces
        
    '''
    if len(n) < k:
        
        n.sort()
        return(n)
    
    test = {}
    size = len(n)//k #length of each part
    for i in range(k): 
        test["n"+str(i)] = mergesort_k(n[i*size:(i+1)*size],k) # Get k slices of len(n)//k length
    
    if len(n) % k != 0:
        test["n"+str(k)] = mergesort_k(n[len(n)-(len(n) % k):],k) # add a slice for the remainder length
    
    result = []
    for i in test.values(): #replace with merge code - should merge the sorted arrays (not ints, arrays)
        for elem in i:
            if result == []:
                result.append(elem) # worked
            else:
                if elem > result[-1]:
                    result.append(elem)
                else:
                    for j in result: #this part is wonky
                        if j > elem:
                            result.insert(result.index(j), elem)
                            break
        
    return result
    
    '''
    test = {}
    size = len(n)//k #length of each part
    for i in range(k): 
        test["n"+str(i)] = n[i*size:(i+1)*size] # Get k slices of len(n)//k length
    
    if len(n) % k != 0:
        test["n"+str(k)] = n[len(n)-(len(n) % k):] # add a slice for the remainder length
    
    result = []
    for i in test.values(): #replace with merge code - should merge the sorted arrays in a dictionary of arrays
        i.sort()
        print(i)
        #result += test(i)
    
    '''    
    

    
def test_sort(n):
    if len(n)<2:
        
        return n
    
    n1 = test_sort(n[:len(n)//2])
    n2 = test_sort(n[len(n)//2:])
    
    result = n1 + n2
    result.sort() #replace with merge code
    return result


    
def msort3(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x) / 2)
    y = msort3(x[:mid])
    z = msort3(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result