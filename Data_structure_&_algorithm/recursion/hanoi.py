# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:18:09 2021

@author: Minzel
"""

def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print("moving from %s to %s" % (a, c))
        hanoi(n-1, b, a, c)
        
        
if __name__ == '__main__':
    hanoi(3, 'A', 'B', 'C')