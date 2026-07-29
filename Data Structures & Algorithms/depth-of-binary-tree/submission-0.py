class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def traversal(node):
            if not node:
                return 0

            left = traversal(node.left)
            right = traversal(node.right)

            return 1 + max(left, right)

        return traversal(root)