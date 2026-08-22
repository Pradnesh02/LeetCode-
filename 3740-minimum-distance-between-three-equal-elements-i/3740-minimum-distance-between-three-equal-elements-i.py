from collections import defaultdict

class Solution(object):
    def minimumDistance(self, nums):
        indices = defaultdict(list)
        for i, val in enumerate(nums):
            indices[val].append(i)
            
        min_dist = float('inf')
        
        for val, idx_list in indices.items():
            # Check every group of 3 consecutive occurrences
            for i in range(len(idx_list) - 2):
                dist = 2 * (idx_list[i + 2] - idx_list[i])
                if dist < min_dist:
                    min_dist = dist
                    
        return min_dist if min_dist != float('inf') else -1