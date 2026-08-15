from collections import Counter

class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        max_val = max(nums1)
        total_good_pairs = 0
        
        for val, freq2 in count2.items():
            step = val * k
            for multiple in range(step, max_val + 1, step):
                if multiple in count1:
                    total_good_pairs += count1[multiple] * freq2
                    
        return total_good_pairs