#!/usr/bin/env python
# coding: utf-8

# In[150]:


import numpy as np


# Problem 3:

# In[151]:


def order_array(input_array):
    """Function takes as input an array of numbers and orders them from smallest to largest
    Input: array
    Output: array ordered (smallest to largest)"""
    
    x = input_array
    
    for i in range(len(x)):    
        for j in range(i+1, len(x)):    
            if(x[i] > x[j]):    
                temp = x[i]  
                x[i] = x[j]    
                x[j] = temp  
    
    return x


# Problem 4:

# In[152]:


from sympy import symbols, Eq, solve


# In[153]:


def kepler_3rd(period):
    """Function takes the orbital period of a planet in years and returns the orbital distance of a planet to the Sun using a derivation of Kepler's 3rd law: (P1)^2/(P2)^2 = (𝛼1)^3/(𝑎2)^3.
    Inputs: Period (Earth days it takes a planet to orbit once), 
    Outputs: Distance from planet to the sun in Astronomical Units (AU)"""
    
    #using earth as a base point
    p1 = 365.25
    a1 = 1
    
    #variables
    p2 = period
    a2 = symbols('a2')
    
    kep3 = Eq((p1**2)/(p2**2),(a1**3)/(a2**3))
    
    solution = solve((kep3),(a2))
    
    x = round(solution[0], 1)
    
    
    return x
    

