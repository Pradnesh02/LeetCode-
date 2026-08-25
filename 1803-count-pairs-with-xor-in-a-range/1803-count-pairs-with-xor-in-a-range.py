from collections import Counter

class Solution(object):
    def countPairs(self, nums, low, high):
        """
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype: int
        """
        def count_less(limit):
            """Counts pairs with XOR < limit using frequency maps"""
            count = 0
            freq = Counter(nums)
            
            while limit > 0:
                next_freq = Counter()
                if limit & 1:
                    # If current bit in limit is 1, XORs that match (limit - 1) are strictly less
                    for val, c in freq.items():
                        count += c * freq.get(val ^ (limit - 1), 0)
                
                # Shift down to check higher order bits
                for val, c in freq.items():
                    next_freq[val >> 1] += c
                    
                freq = next_freq
                limit >>= 1
                
            return count // 2

        # Pairs in [low, high] = (pairs < high + 1) - (pairs < low)
        return count_less(high + 1) - count_less(low)