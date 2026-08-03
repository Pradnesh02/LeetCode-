# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # Traverse both lists until both are exhausted and carry is 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate total sum for current digit position
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Append the new digit node to the result list
            curr.next = ListNode(digit)
            curr = curr.next

            # Advance input list pointers
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next