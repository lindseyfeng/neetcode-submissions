"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {}

        start = head
        new_head = Node(x = 0)
        new_start = new_head


        while start:
            new_node = Node(x = start.val)
            new_start.next = new_node
            dic[start] = new_start.next
            start = start.next
            new_start = new_start.next

        
        start = head
        new_start = new_head.next


        while start:
            if start.random is not None:
                new_start.random = dic[start.random]
            start = start.next
            new_start = new_start.next
        
        return new_head.next




        