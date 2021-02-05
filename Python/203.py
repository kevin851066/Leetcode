# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        '''
        type: head: ListNode
        type : val: int
        rtype: LIstNode
        '''
        d = ListNode(0, head)   # dummy
        output = d
        while d.next:         
            if d.next.val == val:
                d.next = d.next.next
            else:
                d = d.next
        return output.next