class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Compress consecutive equal elements
        dedup = [nums[0]]
        for num in nums[1:]:
            if num != dedup[-1]:
                dedup.append(num)
                
        count = 0
        
        # Check every element with left and right non-equal neighbors
        for i in range(1, len(dedup) - 1):
            if dedup[i - 1] < dedup[i] > dedup[i + 1]:  # Hill
                count += 1
            elif dedup[i - 1] > dedup[i] < dedup[i + 1]:  # Valley
                count += 1
                
        return count