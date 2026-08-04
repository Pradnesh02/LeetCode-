class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_sum = 0
        curr_sum = 0
        freq = {}
        
        for i in range(len(nums)):
            # Add incoming element
            num = nums[i]
            curr_sum += num
            freq[num] = freq.get(num, 0) + 1
            
            # Remove outgoing element when window exceeds length k
            if i >= k:
                out_num = nums[i - k]
                curr_sum -= out_num
                freq[out_num] -= 1
                if freq[out_num] == 0:
                    del freq[out_num]
            
            # If window size is k and all elements are distinct
            if i >= k - 1 and len(freq) == k:
                max_sum = max(max_sum, curr_sum)
                
        return max_sum