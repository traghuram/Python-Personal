#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 17:41:56 2017

@author: taranraghuram
"""

# 1

x = 2
while x <= 10:
    print (x)
    x += 2
    
print('goodbye')

# 2

x = 10
print('Hello!')

while x >= 2:
    print (x)
    x -= 2
    
    
# 3

total = 0
counter = 1

while counter <= end:
    total += counter
    counter += 1

print(total)


# 4

for i in range(2,11,2):
    print(i)

print("Goodbye!")


# 5 

print("Hello!")

for i in range(0,10,2):
    print(10 - i)


# 6

total = 0

for i in range (1, end + 1):
    total += i

print(total)


# imp  - nonintuitive what happens, num gets changed

num = 10
for num in range(5):
    print(num)
print(num)



# 3.guess my number

low = 0
high = 100
guess = (low+high)/2

print("Please think of a number between 0 and 100!")

while True:
    
    guess = int((low+high)/2)
        
    print("Is you secret number " + str(guess) + "?")
    rawInput = input("Enter Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if rawInput not in 'hlc' or len(rawInput) > 1:
        print ("Sorry, I did not understand your input.")
        continue
    
    if rawInput == 'h':
        high = guess
    
    elif rawInput == 'l':
        low = guess
    
    else:
        break
    
print("Game over. The secret number was: " + str(guess))


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0 or len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[len(aStr)//2]:
        return True    
    elif char < aStr[len(aStr)//2]:
        return isIn(char, aStr[0:len(aStr)//2])
    else:
        return isIn(char, aStr[len(aStr)//2:len(aStr)])


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    test = min(a,b)
    gcd = 1
    
    while test > 1:
        if a % test == 0 and b % test == 0 and test > gcd:
            gcd = test
        test -= 1
    
    return gcd




def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    if b == 0:
        gcd = a
        return gcd
    
    return gcdRecur(b, a%b)


def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    
    return aTup[0:len(aTup)+1:2]


def how_many_TR(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    counter = 0
    for n in aDict.values():
        if len(n) == 1:
            counter += 1
        else:
            for i in n:
                counter += 1
    
    return counter


def how_many(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result





def biggestTR(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here

    bDict = []
    cDict = []
    
    for n in aDict:
        bDict.append(n)
        cDict.append(len(aDict[n]))

    return bDict[cDict.index(max(cDict))]



def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result




# Lecture 9

    def __eq__(self, coordinate):
        if self.x == coordinate.x and self.y == coordinate.y:
            return True
        return False
        
    def __repr__(self):
        return 'Coordinate(' + str(self.x) + ',' + str(self.y) + ')'
    


    def intersect(self, s2):
        intersection = []
        for i in self.vals:
            if i in s2 and i not in intersection:
                intersection.append(i)
        
        return intersection
    
    
    def intersect(self, s2):
        intersection = intSet()
        for i in self.vals:
            if i in s2.vals and i not in intersection.vals:
                intersection.vals.append(i)
        
        return intersection
    


# Lecture 10

def genPrimes():
    x = 2
    primes = [2]
    while True:
        counter = 0
        for p in primes:
            if x % p != 0:
                continue
            counter += 1
     
        if counter == 0:
            primes.append(x)
            yield x
        if primes == [2]:
            yield x
        
        x += 1
        
        
        
# Lecture 12

def selSort(L):
    counter = 0
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
        
        counter += 1
    print(counter)


def newSort(L):
    counter = 0
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
            counter += 1
        counter += 1
    print(counter)
    