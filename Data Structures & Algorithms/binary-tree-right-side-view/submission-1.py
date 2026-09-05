# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        result=[]

        while q:
            qlen = len(q)

            for i in range(qlen):
                node = q.popleft()

                if node:
                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

                    # if this is the LAST node of this level
                    if i == qlen - 1:
                        result.append(node.val)
        return result