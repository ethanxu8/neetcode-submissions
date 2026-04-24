# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: 
            return 

        # have slow and fast pointers 
        slow, fast = head, head 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next
        
        # reverse the second half of the list 
        # split two lists 
        prev, curr = None, slow.next
        slow.next = None
        while curr: 
            next_temp = curr.next
            curr.next = prev 
            prev = curr
            curr = next_temp

        # merge first and second 
        first, second = head, prev 
        while second: 
            tmp1, tmp2 = first.next, second.next
            first.next = second 
            second.next = tmp1 
            first, second = tmp1, tmp2

        