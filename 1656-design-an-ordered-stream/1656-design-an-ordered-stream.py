class OrderedStream:

    def __init__(self, n: int):
        # 1-indexed array of size n + 1
        self.stream = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        self.stream[idKey] = value
        chunk = []
        
        # If the inserted key matches the current pointer, collect the contiguous chunk
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            chunk.append(self.stream[self.ptr])
            self.ptr += 1
            
        return chunk