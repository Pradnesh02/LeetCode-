# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev_tail = head  # Node preceding the current group
        group_len = 2     # Target length of the next group (group 1 is size 1, always odd)

        while prev_tail and prev_tail.next:
            # 1. Count the actual number of nodes in the current group
            count = 0
            curr = prev_tail.next
            while count < group_len and curr:
                count += 1
                curr = curr.next

            # 2. If the actual count is even, reverse the nodes in this group
            if count % 2 == 0:
                group_start = prev_tail.next
                curr = group_start
                rev_prev = None

                # Reverse `count` nodes
                for _ in range(count):
                    nxt = curr.next
                    curr.next = rev_prev
                    rev_prev = curr
                    curr = nxt

                # Re-link reversed group with surrounding list
                prev_tail.next = rev_prev
                group_start.next = curr
                
                # Advance prev_tail to the end of the newly reversed group
                prev_tail = group_start
            else:
                # If odd, skip reversing and simply step past the group
                for _ in range(count):
                    prev_tail = prev_tail.next

            group_len += 1

        return head