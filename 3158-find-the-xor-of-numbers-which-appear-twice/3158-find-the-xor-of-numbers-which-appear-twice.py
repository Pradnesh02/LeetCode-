class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        res = 0
        
        for num in nums:
            if num in seen:
                res ^= num
            else:
                seen.add(num)
                
        return res