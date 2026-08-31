import bisect
import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix_sums = []
        total_points = 0

        for a, b, x, y in rects:
            # Count of integer points in [a, x] x [b, y]
            total_points += (x - a + 1) * (y - b + 1)
            self.prefix_sums.append(total_points)

        self.total_points = total_points

    def pick(self) -> List[int]:
        # Pick a target point index uniformly in range [1, total_points]
        target = random.randint(1, self.total_points)
        
        # Locate the rectangle that contains this target point in O(log N)
        rect_idx = bisect.bisect_left(self.prefix_sums, target)
        a, b, x, y = self.rects[rect_idx]

        # Uniformly pick coordinates within that specific rectangle in O(1)
        return [random.randint(a, x), random.randint(b, y)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()