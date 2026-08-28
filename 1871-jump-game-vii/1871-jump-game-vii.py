class Solution:

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # If the last character is '1', we can never land on it
        if s[-1] == "1":
            return False

        n = len(s)
        dp = [False] * n
        dp[0] = True

        # count_reachable maintains the count of reachable indices
        # in the window [i - maxJump, i - minJump]
        count_reachable = 0

        for i in range(1, n):
            # Add entering index into the sliding window
            if i >= minJump and dp[i - minJump]:
                count_reachable += 1

            # Remove exiting index from the sliding window
            if i > maxJump and dp[i - maxJump - 1]:
                count_reachable -= 1

            # If current character is '0' and there is at least one valid jump origin
            if s[i] == "0" and count_reachable > 0:
                dp[i] = True

        return dp[-1]