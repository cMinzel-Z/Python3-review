# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 09:25:03 2020

@author: Minzel
"""
l = ['A', 'B', 'c', 'D']

def changeCase(l):
    for i in range(len(l)):
        if l[i].isupper():
            l[i] = l[i].lower()
        else:
            l[i] = l[i].upper()
    return l