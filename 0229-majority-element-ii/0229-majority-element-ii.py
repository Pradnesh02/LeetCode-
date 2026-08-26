from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # At most 2 elements can appear more than ⌊n / 3⌋ times
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        
        # 1st Pass: Find the top 2 candidate elements using Boyer-Moore
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
                
        # 2nd Pass: Verify the frequencies of candidates
        result = []
        threshold = len(nums) // 3
        
        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > threshold:
                result.append(cand)
                
        return result