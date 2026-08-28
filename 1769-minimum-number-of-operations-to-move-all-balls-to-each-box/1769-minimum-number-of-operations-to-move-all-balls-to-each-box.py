class Solution:

    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        # Left to Right pass: accumulate moves needed for all balls to the left
        count = 0
        moves = 0
        for i in range(n):
            answer[i] += moves
            count += int(boxes[i])
            moves += count

        # Right to Left pass: accumulate moves needed for all balls to the right
        count = 0
        moves = 0
        for i in range(n - 1, -1, -1):
            answer[i] += moves
            count += int(boxes[i])
            moves += count

        return answer