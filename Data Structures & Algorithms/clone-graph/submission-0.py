"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        
        dic = {}
        ls = [node]
        while ls:
            cur = ls.pop()
            if cur and cur not in dic:
                newNode = Node(val = cur.val)
                dic[cur] = newNode
                ls.extend(cur.neighbors)
        
        for k, v in dic.items():
            if k.neighbors:
                temp = []
                for i in k.neighbors:
                    temp.append(dic[i])
                v.neighbors = temp
        
        return dic[node]

