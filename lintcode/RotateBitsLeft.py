# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 20:06:22 2017

@author: jawiezhu
"""

class Solution:
    
    def leftRotate(self,n,d):
        return (n << d) | ( n >> (32-d))
    
if __name__ == '__main__':
    print(5 << 2)