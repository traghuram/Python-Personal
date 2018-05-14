#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 15:56:53 2017

@author: taranraghuram
"""

#New exam

# Problem 1

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    new_text = ''
    
    for i in s:
        if i not in 'aeiouAEIOU':
            new_text += i
    
    print(new_text)


def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    
    new = []
    
    for i in L:
        if L.count(i) % 2 == 1:
            new.append(i)
    
    return max(new)


def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = {}
    difference = {}
    
    for i in d1.keys():
        if i in d2.keys():
            intersect[i] = f(d1[i],d2[i]) #f defined in exam webpage
        else:
            difference[i] = d1[i]
    
    for i in d2.keys():
        if i not in intersect.keys():
            difference[i] = d2[i]
    
    return (intersect, difference)
        

# Problem 3

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    answer = []
    
    for i in s:
        try:
            inty = int(i)
            answer.append(inty)
        except:
            continue
    
    if answer == []:
        raise ValueError
    
    else:
        return sum(answer)

# Problem 4

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    
    max_list_list = []

    def max_list(t, max_list_list):
        
        if type(t) is int:
            max_list_list.append(t)
        
        else:
            for i in t:
                max_list(i, max_list_list)
            
    for i in t:
        max_list(i, max_list_list)
    
    return max(max_list_list)


# Problem 5

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    
    key_code = {}
    
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
    
    decoded = ''
    
    for i in code:
        decoded = decoded + key_code[i]
        
    return (key_code, decoded)
        
    

# Problem 6

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
    
    
    
class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        
        if e in self.vals:
            self.vals[e] -= 1
        

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        
        try:
            return self.vals[e]
        except:
            return 0


    def __add__(self, b1):
        """Returns a new bag that is the union of the other two bags
        """
        c = Bag()
        
        for i in b1.vals:
            c.insert(i)
            try:
                c.vals[i] = b1.vals[i] + self.vals[i]
            
            except:
                c.vals[i] = b1.vals[i]
        
        for i in self.vals:
            if i not in b1.vals:
                c.insert(i)
                c.vals[i] = self.vals[i]
        
        return c
    
    
    
class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        
        del self.vals[e]

    
    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        
        if e in self.vals:
            return True
        
        return False
    

# Problem 7

### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)    



class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        
        self.center_loc = center_loc
        self.tent_loc = tent_loc
        self.tent_list = [tent_loc]
      
        
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        
        # if the new tent is closer than 0.5 units away from any of the current tents, return false
        for i in self.tent_list:
            if new_tent_loc.dist_from(i) < 0.5:
                return False
            
        
        ##place the new tent in the list according to its x-value
        
        #check the current length of the tent list
        len_original = len(self.tent_list)
        len_new = len(self.tent_list)
        
        # add tent location to the list at the index where it finds a value with a larger x coordinate
        for i in self.tent_list:        
            if new_tent_loc.x > i.x:
                continue

            self.tent_list.insert(self.tent_list.index(i),new_tent_loc)
            
            len_new = len(self.tent_list)
            
            break
        
        # if it's bigger than all of the x coordinates, add it to the end
        if len_original == len_new:
            self.tent_list.append(new_tent_loc)
        
        return True
        
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        
        try:
            self.tent_list.remove(tent_loc)
        
        except:
            raise ValueError
        
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        
        string_tent_list = []
        
        for i in self.tent_list:
            string_tent_list.append(str(i))
        
        return string_tent_list
            
