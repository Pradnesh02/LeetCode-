class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        
        for k, trim in queries:
            # Pair each trimmed suffix with its original index
            trimmed = [(num[-trim:], i) for i, num in enumerate(nums)]
            
            # Sort by trimmed string value, ties are broken by index `i` automatically
            trimmed.sort()
            
            # Append the original index of the k-th smallest element (1-indexed)
            ans.append(trimmed[k - 1][1])
            
        return ans