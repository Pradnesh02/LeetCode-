class Solution:
    def checkValidString(self, s: str) -> bool:
        # min_open: minimum possible number of unmatched '('
        # max_open: maximum possible number of unmatched '('
        min_open = 0
        max_open = 0

        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            elif char == '*':
                # '*' can be ')', empty string, or '('
                min_open -= 1  # if '*' acts as ')'
                max_open += 1  # if '*' acts as '('

            # At any point, if the maximum possible '(' is negative,
            # it means there are too many ')' that cannot be matched.
            if max_open < 0:
                return False

            # min_open cannot drop below 0 because '*' can always act as an empty string
            if min_open < 0:
                min_open = 0

        # Valid if it is possible to balance all '(' (i.e. min_open reaches 0)
        return min_open == 0