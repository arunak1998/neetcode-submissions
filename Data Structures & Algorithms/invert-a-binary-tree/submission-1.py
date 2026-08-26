# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def invert(node):
            if not node:
                return

            
            result=TreeNode(node.val)

            result.left=invert(node.right)

            result.right=invert(node.left)


            return result

        return invert(root)

