# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[Treeroot]:
        inorder_index = {
            value: index
            for index, value in enumerate(inorder)
        }

        def dfs(pre_left, pre_right, in_left, in_right):

            # No elements in this subtree
            if pre_left > pre_right:
                return None

            # First element of preorder is the root
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            # Find root position in inorder
            mid = inorder_index[root_val]

            # Number of nodes in left subtree
            left_size = mid - in_left

            # Build left subtree
            root.left = dfs(
                pre_left + 1,
                pre_left + left_size,
                in_left,
                mid - 1
            )

            # Build right subtree
            root.right = dfs(
                pre_left + left_size + 1,
                pre_right,
                mid + 1,
                in_right
            )

            return root

        return dfs(
            0,
            len(preorder) - 1,
            0,
            len(inorder) - 1
        )

        