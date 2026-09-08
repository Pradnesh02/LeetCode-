class RLEIterator:

    def __init__(self, encoding: list[int]):
        self.encoding = encoding
        self.idx = 0

    def next(self, n: int) -> int:
        while self.idx < len(self.encoding):
            # If the current run doesn't have enough elements to satisfy n
            if n > self.encoding[self.idx]:
                n -= self.encoding[self.idx]
                self.idx += 2
            else:
                # The current run can satisfy all remaining n elements
                self.encoding[self.idx] -= n
                return self.encoding[self.idx + 1]

        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)