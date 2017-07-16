# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 12:27:52 2017

@author: traghuram
"""

def minimum_monthly_payment(balance = 0.0, annualInterestRate = 0.0, monthlyPaymentRate = 0.0):
    
    months = 12.0
    monthlyInterestRate = annualInterestRate/months
    monthlyBalance = balance
    
    for m in range(int(months)):

        monthlyBalance = monthlyBalance*(1-monthlyPaymentRate)*(1+monthlyInterestRate)
        
        ''' # old code
        monthlyMinimumPayment = monthlyPaymentRate*monthlyBalance
        monthlyUnpaidBalance = monthlyBalance - monthlyMinimumPayment
        monthlyBalance = monthlyUnpaidBalance*(1+monthlyInterestRate)
        '''
    
    print(round(monthlyBalance,2))
    
    

def fixed_monthly_payment(balance = 0.0, annualInterestRate = 0.0):
    
    months = 12.0
    monthlyInterestRate = annualInterestRate/months
    fixedPayment = 10
    monthlyBalance = balance

    for i in range(int(balance/10)):
        fixedPayment += 10
        monthlyBalance = balance
        print(fixedPayment)
            
        for m in range(int(months)):
            
            unpaidBalance = monthlyBalance - fixedPayment
            monthlyBalance = unpaidBalance*(1 + monthlyInterestRate)
            
            print(monthlyBalance)
          
        if monthlyBalance <= 0:
            return fixedPayment
    


def bisection_payment(balance = 0.0, annualInterestRate = 0.0):
    
    months = 12.0
    monthlyInterestRate = annualInterestRate/months
    monthlyBalance = balance

    lowerBound = balance/12
    upperBound = (balance*(1 + monthlyInterestRate)**12)/12
    fixedPayment = (lowerBound + upperBound)/2
    error = 0.01
    
    while abs(monthlyBalance) > error:
        
        monthlyBalance = balance
        
        for m in range(int(months)):
            
            unpaidBalance = monthlyBalance - fixedPayment
            monthlyBalance = unpaidBalance*(1 + monthlyInterestRate)
        
        if monthlyBalance > 0:
            lowerBound = fixedPayment
        
        else:
            upperBound = fixedPayment
            
        fixedPayment = (lowerBound + upperBound)/2
    
    
    print(round(fixedPayment,2))
          
        



