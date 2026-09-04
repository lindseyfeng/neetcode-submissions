# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        layers = []

        def traverse(root, layer):
            if root:
                if len(layers) <= layer:
                    layers.append([root.val])
                else:
                    layers[layer].append(root.val)
                
                traverse(root.left, layer+1)
                traverse(root.right, layer+1)
        
        traverse(root, 0)
        return layers
        