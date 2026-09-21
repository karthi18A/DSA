# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head to handle edge cases 
        # (e.g., removing the very first node of the list)
        dummy = ListNode(0, head)
        
        # Initialize two pointers, both starting at the dummy node
        slow = dummy
        fast = dummy
        
        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
            
        # Move both pointers simultaneously until fast reaches the last node.
        # This maintains a gap of n between fast and slow.
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        # slow is now at the node immediately before the one we want to remove
        slow.next = slow.next.next
        
        return dummy.next