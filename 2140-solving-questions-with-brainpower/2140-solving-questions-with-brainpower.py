class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = [0] * (n + 1)
        
        # Iterate backwards from the last question
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_idx = i + brainpower + 1
            
            # Points if we solve the question
            solve = points + (dp[next_idx] if next_idx < n else 0)
            
            # Points if we skip the question
            skip = dp[i + 1]
            
            # Maximize current state
            dp[i] = max(solve, skip)
            
        return dp[0]