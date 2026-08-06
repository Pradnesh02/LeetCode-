class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = (total_len + 1) // 2
        
        low, high = 0, m
        
        while low <= high:
            i = (low + high) // 2
            j = half_len - i
            
            # Boundary conditions for nums1
            max_left_1 = nums1[i - 1] if i > 0 else float('-inf')
            min_right_1 = nums1[i] if i < m else float('inf')
            
            # Boundary conditions for nums2
            max_left_2 = nums2[j - 1] if j > 0 else float('-inf')
            min_right_2 = nums2[j] if j < n else float('inf')
            
            # Check if partition is valid
            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                # Odd total elements
                if total_len % 2 == 1:
                    return float(max(max_left_1, max_left_2))
                # Even total elements
                return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2)) / 2.0
            elif max_left_1 > min_right_2:
                high = i - 1
            else:
                low = i + 1