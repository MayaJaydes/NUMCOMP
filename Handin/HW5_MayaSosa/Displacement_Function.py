#!/usr/bin/env python
# coding: utf-8

# In[2]:


def displacement(u_init, t, a):
    """Calculates total displacement of a body during a time interval t
        using initial velocity (speed) and a constant acceleration.
        
        Inputs: Initial Speed[m/s] = u_init 
                Time[s] = t 
                Acceleration [m/s^2] = a (constant)
                
        Outputs: Displacement[m] = s"""
    
    s = (u_init * t) + (0.5 * a * (t**2))
    return s

