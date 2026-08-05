class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        # Case 1: k can be entirely satisfied by 1s
        if k <= numOnes:
            return k
        
        # Case 2: k can be satisfied by 1s and 0s
        if k <= numOnes + numZeros:
            return numOnes
        
        # Case 3: We must pick some -1s
        remaining = k - (numOnes + numZeros)
        return numOnes - remaining