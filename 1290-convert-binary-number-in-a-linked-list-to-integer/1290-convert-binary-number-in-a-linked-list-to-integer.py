# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        res = 0
        p = -1
        node = head

        while node != None:
            p+=1
            node = node.next

        node = head
        
        while node != None and p>-1:
            if node.val == 1:
                res += (node.val)*(2**p)
            p-=1
            node = node.next
            
        return res
            