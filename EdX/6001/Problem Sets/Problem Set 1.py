# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 11:37:23 2017

@author: traghuram
"""


def problem_1_count_vowels(s = 'azcbobobegghakl'):
    
    count = 0
    vowels = 'aeiou'
    
    for char in s:
        if char in vowels:
            count += 1
    
    print("Number of vowels:", count)



def problem_2_find_substring(find = 'bob', s = 'azcbobobobobobobobegghakl'):
    
    count = 0
    num = len(s) - (len(find) - 1)
    
    for i in range(num):
        if find == s[i:i+len(find)]:
            count += 1
    
    print("Number of " + find + ":", count)
    
    
def problem_3_long_substring_alph(s = 'default'):
    
    s = s.lower()
         
    if len(s) < 2:
        return s
    
    longestSubstring = s[0]
    
    for i in range(len(s)): # range goes from i = 0 to len(s) - 1
        if i == 0:
            substring = s[i]
        else:
            if s[i]>=s[i-1]:    # is each letter bigger than or equal to the one prior?
                substring = substring + s[i]
            else:
                substring = s[i]
            if len(substring) > len(longestSubstring):    # is current stored substring stricly longer than stored one?
                longestSubstring = substring
    
    print("Longest substring in alphabetical order is: " + longestSubstring)