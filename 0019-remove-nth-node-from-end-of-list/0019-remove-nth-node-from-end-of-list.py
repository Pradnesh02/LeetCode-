# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

  def removeNthFromEnd(
      self, head: ListNode | None, n: int
  ) -> ListNode | None:
    # Dummy node handles edge cases like removing the head node
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    # Advance fast pointer by n + 1 steps to create a gap of n between slow and fast
    for _ in range(n + 1):
      fast = fast.next

    # Move both pointers until fast reaches the end
    while fast:
      slow = slow.next
      fast = fast.next

    # slow is now just before the node to be removed
    slow.next = slow.next.next

    return dummy.next