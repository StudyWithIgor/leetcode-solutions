'''
O(a+b) time O(a+b) space
a=number of nodes in list 1
b=number of nodes in list 2
'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1 or not l2:
            return l1 if l1 else l2

        dummy=ListNode(None)
        cur=dummy
        p1=l1
        p2=l2
        carry=0

        while p1 or p2 or carry:
            val1=p1.val if p1 else 0
            val2=p2.val if p2 else 0
            total=val1+val2+carry
            
            cur.next=ListNode(total%10)
            cur=cur.next
            carry=total//10

            if p1:
                p1=p1.next

            if p2:
                p2=p2.next

        return dummy.next
