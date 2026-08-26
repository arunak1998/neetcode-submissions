# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=0

        def traverse(node):
            nonlocal maxi
            if not node:
                return 0


            left=traverse(node.left)
            right=traverse(node.right)



            maxi=max(maxi,left+right)

            return 1+max(left,right)


        traverse(root)
        return maxi