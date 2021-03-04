# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 09:26:40 2020

@author: Minzel
"""

def type_check(b):
    if b != []:
        for i in range(len(b)):
            if type(b[i]) != type(b[0]):
                return False
        return True
    else:
        return 0

print(type_check([1,2,3,'3',5]))