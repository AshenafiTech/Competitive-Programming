# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA==None or headB==None:
            return None

        a, b = 0, 0
        p, q = headA, headB

        while p!=None:
            a+=1
            p=p.next
        while q!=None:
            b+=1
            q=q.next

        p, q = headA, headB

        if a>b:
            for _ in range(a-b):
                p = p.next

        elif a<b:
            for _ in range(b-a):
                q = q.next
        while p != q:
            p=p.next
            q=q.next

        if p==q:
            return q