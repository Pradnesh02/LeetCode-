import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        """
        Reservoir Sampling algorithm:
        Ensures each node has an equal 1/N probability of being chosen
        using O(1) extra space.
        """
        chosen_val = 0
        curr = self.head
        scope = 1

        while curr:
            # Pick current node with probability 1 / scope
            if random.random() < 1.0 / scope:
                chosen_val = curr.val
            scope += 1
            curr = curr.next

        return chosen_val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()