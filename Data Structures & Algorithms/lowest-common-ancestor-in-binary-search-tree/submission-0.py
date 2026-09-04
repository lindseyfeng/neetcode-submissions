# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traverse(cur, ls, target):
            if cur:
                ls.append(cur)
                if cur == target: return ls

                l1 = traverse(cur.left,ls.copy(), target)
                l2 = traverse(cur.right,ls.copy(), target)
                if l1: return l1
                if l2: return l2
        
        l1 = traverse(root, [], p)
        l2 = traverse(root, [], q)

        for i in range(min(len(l1), len(l2))):
            if l1[i] == l2[i]:continue
            else: return l1[i-1]
        return l1[i]
            
        