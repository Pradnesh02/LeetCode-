class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        total_beams = 0
        prev_count = 0

        for row in bank:
            # Count the number of devices ('1's) in the current row
            curr_count = row.count('1')
            
            # Only connect with rows that have at least one device
            if curr_count > 0:
                total_beams += prev_count * curr_count
                prev_count = curr_count

        return total_beams