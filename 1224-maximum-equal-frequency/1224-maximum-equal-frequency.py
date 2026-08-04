from collections import defaultdict

class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = defaultdict(int)
        freq_count = defaultdict(int)
        max_freq = 0
        ans = 0
        
        for i, num in enumerate(nums):
            # Update frequency maps
            if count[num] > 0:
                freq_count[count[num]] -= 1
                
            count[num] += 1
            curr_freq = count[num]
            freq_count[curr_freq] += 1
            
            max_freq = max(max_freq, curr_freq)
            
            # Condition 1: max_freq == 1 (all numbers occur once)
            cond1 = (max_freq == 1)
            
            # Condition 2: One number has frequency 1, rest have max_freq
            cond2 = (freq_count[1] == 1 and freq_count[max_freq] * max_freq + 1 == i + 1)
            
            # Condition 3: One number has max_freq, rest have (max_freq - 1)
            cond3 = (freq_count[max_freq] == 1 and 
                     freq_count[max_freq - 1] * (max_freq - 1) + max_freq == i + 1)
            
            if cond1 or cond2 or cond3:
                ans = i + 1
                
        return ans