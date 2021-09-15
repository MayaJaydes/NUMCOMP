#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Problem 3
def acceleration(u1, u2, t1, t2):
    """Calculates acceleration of a body using different speeds at different times
    Inputs: Speed 1 [u1] and Speed 2 [u2] = m/s ; Time 1 [t1] and Time 2 [ts] = s
    Output: Acceleration [a] = m/s^2"""

    a = (u2 - u1) / (t2 - t1)
    return a

