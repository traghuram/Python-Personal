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