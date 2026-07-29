class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        
        while i < n1 and j < n2:
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            
            if id1 == id2:
                res.append([id1, val1 + val2])
                i += 1
                j += 1
            elif id1 < id2:
                res.append([id1, val1])
                i += 1
            else:
                res.append([id2, val2])
                j += 1
                
        # Append remaining elements from nums1 if any
        while i < n1:
            res.append(nums1[i])
            i += 1
            
        # Append remaining elements from nums2 if any
        while j < n2:
            res.append(nums2[j])
            j += 1
            
        return res