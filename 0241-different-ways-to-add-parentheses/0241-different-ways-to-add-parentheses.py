class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        memo = {}

        def compute(expr):
            if expr in memo:
                return memo[expr]

            res = []
            for i, char in enumerate(expr):
                if char in "+-*":
                    # Divide into left and right sub-expressions
                    left_res = compute(expr[:i])
                    right_res = compute(expr[i+1:])

                    # Combine results from left and right sub-expressions
                    for l in left_res:
                        for r in right_res:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)

            # Base case: purely numeric expression without operators
            if not res:
                res = [int(expr)]

            memo[expr] = res
            return res

        return compute(expression)