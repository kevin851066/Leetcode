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
        v1, v2 = [], []
        while l1:
            v1.append(l1.val)
            l1 = l1.next
        while l2:
            v2.append(l2.val)
            l2 = l2.next
        
        len1, len2 = len(v1), len(v2)
        v1, v2 = v1[::-1], v2[::-1]
        i, carry_i = 0, 0
        m = max(len1, len2)
        s = []
        while i < m or carry_i:
            if i < len1:
                carry_i += v1[i]
            if i < len2:
                carry_i += v2[i]
            s.append(carry_i % 10)
            carry_i //= 10
            i += 1
            
        s = s[::-1]
        lens = len(s)
        dummy = curr = ListNode(0)
        j = 0
        while j < lens:
            curr.next = ListNode(s[j])
            curr = curr.next
            j += 1
        return dummy.next