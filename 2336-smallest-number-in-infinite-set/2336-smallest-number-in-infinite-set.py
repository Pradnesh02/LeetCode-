import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.current = 1
        self.added_back = []
        self.added_set = set()

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.added_back:
            smallest = heapq.heappop(self.added_back)
            self.added_set.remove(smallest)
            return smallest
        
        smallest = self.current
        self.current += 1
        return smallest

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Only add back if the number was previously popped and is not already added
        if num < self.current and num not in self.added_set:
            heapq.heappush(self.added_back, num)
            self.added_set.add(num)