# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def traverse(root, cur_max):
            nonlocal ans
            if root:
                if root.val >= cur_max:
                    ans +=1
                    cur_max = root.val
                traverse(root.left, cur_max)
                traverse(root.right, cur_max)
        
        traverse(root, -math.inf)
        return ans