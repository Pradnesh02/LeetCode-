class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # Maps prefix_sum -> index
        prefix_map = {0: -1}
        curr_sum = 0
        ans = float('inf')
        
        # min_len[i] stores the minimum length of a valid subarray found in arr[0...i]
        min_len = [float('inf')] * len(arr)
        
        for i, val in enumerate(arr):
            curr_sum += val
            needed = curr_sum - target
            
            # Carry forward the best length seen so far
            prev_best = min_len[i - 1] if i > 0 else float('inf')
            
            if needed in prefix_map:
                start_idx = prefix_map[needed]
                curr_sub_len = i - start_idx
                
                # If a valid non-overlapping subarray exists prior to this one
                if start_idx >= 0 and min_len[start_idx] != float('inf'):
                    ans = min(ans, curr_sub_len + min_len[start_idx])
                
                min_len[i] = min(prev_best, curr_sub_len)
            else:
                min_len[i] = prev_best
                
            prefix_map[curr_sum] = i
            
        return ans if ans != float('inf') else -1