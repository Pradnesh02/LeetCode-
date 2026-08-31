import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenations in different orders aren't equal, no common divisor exists
        if str1 + str2 != str2 + str1:
            return ""
        
        # The length of the GCD string is the GCD of their lengths
        gcd_len = math.gcd(len(str1), len(str2))
        return str1[:gcd_len]