# -*- coding: utf-8 -*-
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