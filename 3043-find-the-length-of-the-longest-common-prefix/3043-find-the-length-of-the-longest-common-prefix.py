class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefixes = set()
        
        # Step 1: Insert all prefixes of numbers in arr1 into the set
        for num in arr1:
            val = str(num)
            for i in range(1, len(val) + 1):
                prefixes.add(val[:i])
                
        max_len = 0
        
        # Step 2: Check all prefixes of numbers in arr2 against the set
        for num in arr2:
            val = str(num)
            for i in range(len(val), 0, -1):
                if val[:i] in prefixes:
                    max_len = max(max_len, i)
                    break  # Longest possible prefix found for this number
                    
        return max_len