class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Step 1: XOR all elements to get a ^ b
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
            
        # Step 2: Get the rightmost set bit
        diff = xor_sum & (-xor_sum)
        
        # Step 3: Separate the numbers into two groups and find a and b
        a, b = 0, 0
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num
                
        return [a, b]