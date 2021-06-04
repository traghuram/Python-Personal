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
import time


x_pset = 3141592653589793238462643383279502884197169399375105820974944592
y_pset = 2718281828459045235360287471352662497757247093699959574966967627



def week_1(n = [7,6,5,4,3,2,1]*5000, k=4, x = x_pset, y=y_pset):
    
    '''
    for i in range(k):
        start = time.time()
        mergesort_k(n,i+2)
        end = time.time()
        print("mergesort", i+2, end - start)
    '''
    
    start = time.time()
    mergesort(n)
    end = time.time()
    print("mergesort normal", end - start)
    
    print("Karatsuba: ", karatsuba(x,y))
    print("Normal: ", x*y)



def karatsuba(x, y):
    '''
    Recursive multiplication, but with three recursive calls
    Assumes inputs are integers
    '''
        
    if x < 10 or y < 10:
        return x*y
    
    max_len = max(len(str(x)), len(str(y)))
    half = max_len//2
    power = max_len - half
    
    #if x or y has fewer than the power number, do something (return answer?)
    if len(str(x)) <= power or len(str(y)) <= power:
        return x*y
    
    a = int(str(x)[:-power])
    b = int(str(x)[-power:])
    c = int(str(y)[:-power])
    d = int(str(y)[-power:])
    
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_bc = karatsuba((a+b),(c+d))
        
    return 10**(2*power)*ac + 10**power*(ad_bc - ac - bd) + bd


def karatsuba_lite(x, y):
    '''
    Recursive multiplication, but with four recursive calls
    Assumes inputs are integers
    '''
        
    if x < 10 or y < 10:
        return x*y
    
    x_half = len(str(x))//2
    y_half = len(str(y))//2
    x_power = len(str(x)) - x_half
    y_power = len(str(y)) - y_half
    
    a = int(str(x)[:x_half])
    b = int(str(x)[x_half:])
    c = int(str(y)[:y_half])
    d = int(str(y)[y_half:])
                
    ac = karatsuba_lite(a,c)
    ad = karatsuba_lite(a,d)
    bc = karatsuba_lite(b,c)
    bd = karatsuba_lite(b,d)
        
    return 10**(x_power+y_power)*ac + 10**(x_power)*ad + 10**(y_power)*bc + bd



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
    
    if k < 2:
        return "Pick another k dumbass"
    
    
    if len(n) < k:
        
        n.sort()
        return(n)
    
    test = {}
    size = len(n)//k #length of each part
    for i in range(k): 
        test["n"+str(i)] = mergesort_k(n[i*size:(i+1)*size],k) # Get k slices of len(n)//k length
    
    if len(n) % k != 0:
        test["n"+str(k)] = mergesort_k(n[len(n)-(len(n) % k):],k) # add a slice for the remainder length
    
    
    result = test.pop("n0")
    for array in test.values():
        holder = []
        i = 0
        j = 0
            
        while i < len(result) and j < len(array):
            if result[i] > array[j]:
                holder.append(array[j])
                j += 1
            else:
                holder.append(result[i])
                i += 1
                
        holder += result[i:]
        holder += array[j:]
        result = holder[:]
    
    return result