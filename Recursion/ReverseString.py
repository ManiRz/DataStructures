#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:03:58 2020

@author: subramaniam.s
"""

def print_string(string):
    if len(string) == 0:
        return string
    else:
        print(string)
        return print_string(string[1:]) + string[0]
    
    
    
reversed_string = print_string('subramaniam')
print(reversed_string)