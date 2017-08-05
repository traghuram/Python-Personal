#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 13:23:26 2017

@author: taranraghuram
"""

import numpy as np


def problem_1():
    Y = np.matrix( ((15.1,), (7.9,), (4.5,), (12.8,), (10.5,)) )
    
    X = np.matrix( ((1, 25.5, 1.23), (1, 40.8, 1.89), (1, 30.2, 1.55), (1, 4.3, 1.18), (1, 10.7, 1.68)) )
    
    b1 = np.matrix( ((23,), (0.1,), (-8.0,)) )
    
    b2 = np.matrix( ((22,), (-0.2,), (-7,)) )
    
    e1 = Y - X*b1
    
    e2 = Y - X*b2
    
    # problem 2
    if sum(abs(e1)) < sum(abs(e2)):
        print('e1 is smaller: \n', e1)
    
    else:
        print('e2 is smaller: \n', e2)
        
        
# problem