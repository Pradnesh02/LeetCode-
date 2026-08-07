class Solution(object):
    def maxSumDistinctTriplet(self, x, y):
        """
        :type x: List[int]
        :type y: List[int]
        :rtype: int
        """
        # Step 1: Map each distinct x-value to its maximum y-value
        max_y_for_x = {}
        for xi, yi in zip(x, y):
            if xi not in max_y_for_x or yi > max_y_for_x[xi]:
                max_y_for_x[xi] = yi

        # Step 2: If we have fewer than 3 distinct x-values, a triplet cannot be formed
        if len(max_y_for_x) < 3:
            return -1

        # Step 3: Get the top 3 largest y-values from distinct x-values
        top_3_y = sorted(max_y_for_x.values(), reverse=True)[:3]

        return sum(top_3_y)