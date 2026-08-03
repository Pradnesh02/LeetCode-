class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Edge case: multiplying by zero yields "0"
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        # The result of multiplying m-digit and n-digit numbers can be at most (m + n) digits
        res = [0] * (m + n)

        # Multiply each digit from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Multiply corresponding single digits
                mul = int(num1[i]) * int(num2[j])
                
                # Positions in the result array:
                # p2 is the current position, p1 is the carry position
                p1, p2 = i + j, i + j + 1
                
                # Add product to current value at p2
                total = mul + res[p2]
                
                # Update positions with carry and remaining digit
                res[p2] = total % 10
                res[p1] += total // 10

        # Skip leading zeros if present at index 0
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1

        # Convert result array back to string
        return "".join(map(str, res[start:]))