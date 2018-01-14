# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 19:42:31 2017

@author: jawiezhu
"""

class Solution:
    def twoSum(self,nums,target):
        left = 0
        right = len(nums) -1
        
        while( nums[left] + nums[right] != target):
            if ( nums[left] + nums[right] > target):
                right = right - 1
            if ( nums[left] + nums[right] < target):
                left = left + 1
     
        return left + 1,right + 1