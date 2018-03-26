# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:08:06 2017

@author: traghuram
"""

#from src import Config as cg
import pandas as pd
import numpy as np

class Distribution:
    
    def __init__(self, name="Default", raw_data = False):
        #"sds"
        #"sd"
        self.name = name
        self.table = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
        
    def __str__(self, year=0):
        return self.name
    
    def show_data():
        
        
    def export_data(self,year1=0, year2=0):
        
        
    def project_out_distribution(self, years = 10):