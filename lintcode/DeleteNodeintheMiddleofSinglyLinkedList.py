# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 19:13:41 2017

@author: jawiezhu
"""

class ListNode(object):
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        

class Solution:
    
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next