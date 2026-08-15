class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_count = [0] * k
        
        for num in arr:
            remainder_count[num % k] += 1
            
        # Remainder 0 must appear an even number of times
        if remainder_count[0] % 2 != 0:
            return False
            
        # Remainder r must match remainder (k - r)
        for r in range(1, (k // 2) + 1):
            if remainder_count[r] != remainder_count[k - r]:
                return False
                
        return True