class Solution:
    def isPalindrome(self, head):
        '''
        :type: head: ListNode
        :rtype: bool
        '''
        s = []
        while head:
            s.append(head.val)
            head = head.next
        return s == s[::-1]
            