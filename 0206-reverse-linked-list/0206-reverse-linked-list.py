class Solution(object):
    def reverseList(self, head):
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        
        # Reverse the link between head.next and head
        head.next.next = head
        head.next = None
        
        return new_head