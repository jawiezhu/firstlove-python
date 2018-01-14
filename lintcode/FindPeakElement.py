

class Solution:
	def findPeak_TimeOut(self,A):
		for i in range(1, len(A)-1):
			if(A[i] > A[i-1] and A[i] > A[i+1]):
			    return i

			    
	def findPeak(self, A):
		left = 0
		right = len(A) - 1
		while( left <= right):
			if( left == right):
				return left
			mid = (left + right)/2
			if( A[mid] < A[mid+1]):
				left = mid + 1
			else: 
				right = mid
