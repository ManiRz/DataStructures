#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:31:16 2020

@author: subramaniam.s
"""




def print_array(arr,index):
    if index>=len(arr):
        return 
    print(arr[len(arr)-1-index])
    print_array(arr,index+1)
    
print_array([1,2,3,4,5,6,7],0)
