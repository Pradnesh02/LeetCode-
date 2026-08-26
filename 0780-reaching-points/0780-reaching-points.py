class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # Work backwards from (tx, ty) towards (sx, sy)
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            
            if tx > ty:
                # If ty matches sy, check if the remaining diff in x is divisible by ty
                if ty == sy:
                    return (tx - sx) % ty == 0
                tx %= ty
            else:
                # If tx matches sx, check if the remaining diff in y is divisible by tx
                if tx == sx:
                    return (ty - sy) % tx == 0
                ty %= tx
                
        return False