class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            result.append(chr(ord('A') + rem))
            columnNumber //= 26
            
        return "".join(reversed(result))