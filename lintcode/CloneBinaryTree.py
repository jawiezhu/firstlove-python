# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 21:39:58 2017

@author: jawiezhu
"""

class TreeNode:
    def __init__(self,val):
        this.val = val
        this.left, this.right = None, None
        
class Solution:
    
    def cloneTree(self,root):
        if root is None:
            return None
        newRoot = TreeNode(root.val)
        newRoot.left = self.cloneTree(root.left)
        newRoot.right = self.cloneTree(root.right)
        return newRoot