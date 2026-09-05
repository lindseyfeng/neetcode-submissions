class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def traverse(root, cur_left, cur_right):
            if not root:
                return True

            if root.val <= cur_left or root.val >= cur_right:
                return False

            return (
                traverse(root.left, cur_left, root.val)
                and
                traverse(root.right, root.val, cur_right)
            )

        return traverse(root, -math.inf, math.inf)