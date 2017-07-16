# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 12:40:06 2017

@author: traghuram
"""
import pandas as pd
import numpy as np


def greet(lang, person):
    if lang == 'es':
        return 'Hola ' + person
    else:
        return 'Hello ' + person
    
    
def set(num):
    for n in num:
        print (n**2)
    print ('done')
    
    
def sample():
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue #shortcut to next iteration of loop
        print("Found a number", num)
        
        
        
def make_incrementor(n):
    return lambda x: x + n
