# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # The first bad version is at 'mid' or to its left
                right = mid
            else:
                # The first bad version must be to the right of 'mid'
                left = mid + 1
                
        return left