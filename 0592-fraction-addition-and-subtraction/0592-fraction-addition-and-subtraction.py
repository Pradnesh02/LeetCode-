def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # Replace '-' with '+-' to easily split terms by '+'
        formatted_expr = expression.replace('-', '+-')
        terms = formatted_expr.split('+')
        
        A, B = 0, 1  # Running fraction A / B
        
        for term in terms:
            if not term:
                continue
            
            num, den = map(int, term.split('/'))
            
            # Cross-multiply to add fractions: A/B + num/den
            A = A * den + num * B
            B = B * den
            
        # Reduce the resulting fraction using our custom GCD
        common_gcd = gcd(abs(A), B)
        A //= common_gcd
        B //= common_gcd
        
        return "{}/{}".format(A, B)