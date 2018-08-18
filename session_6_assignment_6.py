# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 22:50:58 2018

@author: disiz
"""
import numpy as np
print(np.__version__)
"""Session 6
Assignment SIX"""
#CODE FOR QUESTION 1
def Vandermonde(x,N,bool=False):
    """defining a function with 3 arguments x being array of elements,
     N by default being length of array which can be overwritten,
     final argument being boolean either True (for increasing powers) 
     or False (for decreasing powers which is default)"""
    if bool==0:
        return np.column_stack([x**(N-1-i) for i in range(N)])
               
    elif bool==1:
        return np.column_stack([x**(i) for i in range(N)])
    else:
        print("value of bool to be STRICTLY either 0 or 1") 
lst=np.array([1,2,3,4,5])
N=len(lst)
help(Vandermonde)
print("*/ assignment 6 output 1/*")
print("Alexandre- Theophile Vandermonde Matrix\n")
print("\twith decreasing powers:\n",Vandermonde(lst,N))
print("*/ assignment 6 output 1/*")
print("\twith increasing powers:\n",Vandermonde(lst,N,3))
print("\nEnd of assignment")
        
