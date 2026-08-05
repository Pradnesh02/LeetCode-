class Solution(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        num1, num2 = expression.split('+')
        min_val = float('inf')
        best_expr = ""
        
        # Try all valid positions for '(' in num1
        for i in range(len(num1)):
            left_mul_str = num1[:i]
            left_add_str = num1[i:]
            
            left_mul = int(left_mul_str) if left_mul_str else 1
            left_add = int(left_add_str)
            
            # Try all valid positions for ')' in num2
            for j in range(1, len(num2) + 1):
                right_add_str = num2[:j]
                right_mul_str = num2[j:]
                
                right_add = int(right_add_str)
                right_mul = int(right_mul_str) if right_mul_str else 1
                
                val = left_mul * (left_add + right_add) * right_mul
                
                if val < min_val:
                    min_val = val
                    best_expr = "{}({}+{}){}".format(
                        left_mul_str, left_add_str, right_add_str, right_mul_str
                    )
                    
        return best_expr