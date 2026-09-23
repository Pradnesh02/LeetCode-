class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        
        # Frequency array for remainders 0 to k - 1
        # Initialize remainder 0 with count 1 to handle subarrays starting at index 0
        remainder_counts = [0] * k
        remainder_counts[0] = 1
        
        for num in nums:
            current_sum += num
            rem = current_sum % k
            
            # Every previous prefix sum with the same remainder forms a valid subarray
            count += remainder_counts[rem]
            remainder_counts[rem] += 1
            
        return count