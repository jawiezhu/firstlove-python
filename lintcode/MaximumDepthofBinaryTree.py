class TreeNode:
	def __init__(self,val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def maxDepth(self, root):
		if root is None:
			return 0
		leftDepth = self.maxDepth(root.left)
		rightDepth = self.maxDepth(root.right)
		#return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
		return max(leftDepth,rightDepth) + 1
		