# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy
        
        # Traverse while there are at least two nodes left to swap
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            # Perform the pointer adjustments
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Advance prev to the node before the next pair
            prev = first
            
        return dummy.next