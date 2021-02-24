# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        '''
        :type: l1: ListNode
        :type: l2: ListNode
        :rtype: ListNode
        '''
        dummy = cur = ListNode(0)
        carry = 0
        while l1 != None or l2 != None or carry:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
                
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
            
        return dummy.next