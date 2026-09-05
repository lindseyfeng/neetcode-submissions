class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ls = []

        def traverse(root):
            if not root:
                return

            traverse(root.left)

            if len(ls) >= k:
                return

            ls.append(root.val)

            traverse(root.right)

        traverse(root)
        return ls[k - 1]