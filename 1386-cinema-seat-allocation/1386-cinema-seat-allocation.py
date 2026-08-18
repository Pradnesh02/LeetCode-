from collections import defaultdict

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        # Store occupied seats for rows that have reservations
        rows = defaultdict(set)
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                rows[row].add(col)
                
        # Rows with zero reservations in columns 2-9 can each take 2 families
        ans = (n - len(rows)) * 2
        
        # Check rows that have reserved seats
        for reserved in rows.values():
            left = not any(c in reserved for c in (2, 3, 4, 5))
            right = not any(c in reserved for c in (6, 7, 8, 9))
            middle = not any(c in reserved for c in (4, 5, 6, 7))
            
            if left and right:
                ans += 2
            elif left or right or middle:
                ans += 1
                
        return ans