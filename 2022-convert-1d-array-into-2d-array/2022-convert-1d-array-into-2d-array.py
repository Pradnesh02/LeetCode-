class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        # If total number of elements doesn't match m * n, construction is impossible
        if len(original) != m * n:
            return []
            
        # Slice original into m rows, each of length n
        return [original[i * n : (i + 1) * n] for i in range(m)]