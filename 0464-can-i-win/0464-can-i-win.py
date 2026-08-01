class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        # If desired total is <= 0, the first player wins immediately
        if desiredTotal <= 0:
            return True

        # Calculate the sum of all numbers available in the pool
        total_sum = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2

        # If the sum of all numbers is less than desiredTotal, no one can win
        if total_sum < desiredTotal:
            return False

        # Memoization dictionary: state (bitmask of chosen numbers) -> bool
        memo = {}

        def can_win(used_mask, current_total):
            if used_mask in memo:
                return memo[used_mask]

            for i in range(1, maxChoosableInteger + 1):
                # Check if the number 'i' has not been used yet
                if not (used_mask & (1 << i)):
                    # Winning move: choosing 'i' reaches or exceeds desiredTotal
                    if current_total + i >= desiredTotal:
                        memo[used_mask] = True
                        return True

                    # Opponent's turn: if choosing 'i' forces opponent into a losing position, current player wins
                    if not can_win(used_mask | (1 << i), current_total + i):
                        memo[used_mask] = True
                        return True

            memo[used_mask] = False
            return False

        return can_win(0, 0)