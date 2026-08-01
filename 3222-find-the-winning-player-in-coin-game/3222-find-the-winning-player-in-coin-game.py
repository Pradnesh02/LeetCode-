class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        # Each turn requires exactly 1 coin of value 75 and 4 coins of value 10
        # Total value = 75 * 1 + 10 * 4 = 115
        turns = min(x, y // 4)
        
        # If the number of possible turns is odd, Alice takes the last turn and wins.
        # If even, Bob takes the last turn (or Alice has no moves at start) and Bob wins.
        return "Alice" if turns % 2 == 1 else "Bob"