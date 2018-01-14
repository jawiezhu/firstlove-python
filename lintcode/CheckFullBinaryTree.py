# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 10:21:33 2017

@author: jawiezhu
"""


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None
        
class Solution:
    def isFullTree(self, root):
        if root is None: return False
        