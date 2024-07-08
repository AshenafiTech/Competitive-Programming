# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return None
        
        while head != None and head.val == val:
            head = head.next
            
        itr = head
        
        while itr != None and  itr.next != None:
            if itr.next.val == val:
                itr.next = itr.next.next
            else:
                itr = itr.next
                
        return head
                