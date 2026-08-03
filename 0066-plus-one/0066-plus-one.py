class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        # Traverse the list in reverse starting from the least significant digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If digit is 9, it becomes 0 and carry continues to the left
            digits[i] = 0
            
        # If all digits were 9 (e.g., [9, 9, 9] -> [0, 0, 0]), prepend a 1 at the front
        return [1] + digits