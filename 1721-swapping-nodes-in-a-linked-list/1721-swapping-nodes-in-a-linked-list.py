# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

  def swapNodes(
      self, head: Optional[ListNode], k: int
  ) -> Optional[ListNode]:
    first = head

    # Advance `first` to the k-th node from the beginning (1-indexed)
    for _ in range(k - 1):
      first = first.next

    # Use a two-pointer approach to find the k-th node from the end
    curr = first
    second = head
    while curr.next:
      curr = curr.next
      second = second.next

    # Swap the values between the k-th node from the start and the k-th from the end
    first.val, second.val = second.val, first.val

    return head