
class Solution:

	def __init__(self):
		pass

	def maxProfit(self, prices):
		maxprofit = 0
		for i in range(0, len(prices)-1):
			if(prices[i+1] - prices[i] > 0):
				maxprofit = maxprofit  + ( prices[i+1] - prices[i])
			else:
				continue
		return maxprofit 