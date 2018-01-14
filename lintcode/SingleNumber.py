# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:00:13 2017

@author: jawiezhu
"""

class Solution:
    def singleNumber(self,A):
        dict = {}
        
        for i in range(0,len(A)):
            if dict.__contains__(A[i]) == False:
                dict[A[i]] =  1
                continue
            
            if(dict[A[i]] == 1):
                dict[A[i]] = dict[A[i]] + 1
            
        print(dict)
        for (k,v) in dict.items():
            if v == 1:
                return int(k)
                

if __name__ == "__main__":
    dict = {}
    A = [1,2,3,3,4,5]
    #dict[A[2]] = 1
    #del(dict[A[2]])
    s = Solution()
    
    s.singleNumber(A)
    
    print(dict.__contains__(A[2]))