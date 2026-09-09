class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        upper = 10**n - 1
        lower = 10 ** (n - 1)

        # Iterate through the upper half of the palindrome in descending order
        for left in range(upper, lower - 1, -1):
            # Construct an even-length palindrome from the left half
            palindrome = int(str(left) + str(left)[::-1])

            # Check if it factors into two n-digit numbers
            factor = upper
            while factor * factor >= palindrome:
                if palindrome % factor == 0:
                    other_factor = palindrome // factor
                    if lower <= other_factor <= upper:
                        return palindrome % 1337
                factor -= 1

        return 0