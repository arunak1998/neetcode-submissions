# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal maxi
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            maxi = max(maxi, left + right)

            return max(left, right) + 1
        maxi=float('-inf')
        dfs(root)

        return maxi