# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:41:55 2017

@author: jawiezhu
"""

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None
        
class Solution:
    def invertBinaryTree(self, root):
        if root is None: 
            return None
        root.left,root.right = self.invertBinaryTree(root.right),self.invertBinaryTree(root.left)
        return root
    
    
    def invertBinaryTree_2(self,root):
        self.dfs(root)
    
    def dfs(self,node):
        left = node.left
        right = node.right
        node.left = right
        node.right = left
        
        if (left != None): self.dfs(left)
        if (right != None): self.dfs(right)