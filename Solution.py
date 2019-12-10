# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        l3 = ListNode(0)
        cur = l3
        while l1 or l2:
            node = ListNode(carry)
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            if node.val >= 10:
                carry = 1
            else:
                carry = 0
            node.val %= 10
            cur.next, cur = node, node 
        if carry:
            cur.next = ListNode(1)
        return(l3.next)
