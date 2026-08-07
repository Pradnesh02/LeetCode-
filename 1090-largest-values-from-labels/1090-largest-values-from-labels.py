from collections import defaultdict

class Solution(object):
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type numWanted: int
        :type useLimit: int
        :rtype: int
        """
        # Pair values with labels and sort by values in descending order
        items = sorted(zip(values, labels), key=lambda x: x[0], reverse=True)
        
        label_counts = defaultdict(int)
        total_sum = 0
        items_selected = 0
        
        for val, label in items:
            if items_selected == numWanted:
                break
                
            # Check if this label can still be used
            if label_counts[label] < useLimit:
                total_sum += val
                label_counts[label] += 1
                items_selected += 1
                
        return total_sum