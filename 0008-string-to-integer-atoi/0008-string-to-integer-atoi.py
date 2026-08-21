class Solution(object):
    def myAtoi(self, s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)

        # 1. Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0

        # 2. Determine sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # 3. Read digits and compute result
        val = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            val = val * 10 + digit
            i += 1

        # Apply sign
        val = sign * val

        # 4. Clamp to 32-bit signed integer range
        if val < INT_MIN:
            return INT_MIN
        if val > INT_MAX:
            return INT_MAX

        return val