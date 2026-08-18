class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        good_pairs = 0
        
        for x in nums1:
            for y in nums2:
                divisor = y * k
                if x % divisor == 0:
                    good_pairs += 1
                    
        return good_pairs