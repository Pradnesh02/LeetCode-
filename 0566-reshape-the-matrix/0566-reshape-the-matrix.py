class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        
        # Check if total number of elements matches
        if m * n != r * c:
            return mat
            
        # Initialize output matrix of size r x c
        ans = [[0] * c for _ in range(r)]
        
        # Populate new matrix using flattened index mapping
        for k in range(m * n):
            ans[k // c][k % c] = mat[k // n][k % n]
            
        return ans