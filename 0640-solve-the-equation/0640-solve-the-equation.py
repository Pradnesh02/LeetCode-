class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        def parse(expr):
            x_coeff = 0
            const_val = 0
            
            # Format expression to easily split terms by '+'
            expr = expr.replace('-', '+-')
            terms = expr.split('+')
            
            for term in terms:
                if not term:
                    continue
                if term.endswith('x'):
                    val = term[:-1]
                    if not val or val == '+':
                        x_coeff += 1
                    elif val == '-':
                        x_coeff -= 1
                    else:
                        x_coeff += int(val)
                else:
                    const_val += int(term)
                    
            return x_coeff, const_val

        left_side, right_side = equation.split('=')
        
        left_x, left_const = parse(left_side)
        right_x, right_const = parse(right_side)
        
        # Move all x terms to the left and constants to the right
        total_x = left_x - right_x
        total_const = right_const - left_const
        
        if total_x == 0:
            if total_const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
                
        return "x=" + str(total_const // total_x)