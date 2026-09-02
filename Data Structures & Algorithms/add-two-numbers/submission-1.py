# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def number(l):
            cur = ""
            while l:
                cur = str(l.val)+cur
                l = l.next
            return cur
        
        l1_digits = number(l1)
        l2_digits = number(l2)

        ans = list(str(int(l1_digits)+int(l2_digits)))

        dummy = ListNode()
        start = dummy
        
        while ans:
            i = ans.pop()
            new_node = ListNode(val = i)
            start.next = new_node
            start = start.next
        
        return  dummy.next


        