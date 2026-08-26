# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q=deque([root])

        result=[]
        while q:

            length=len(q)

            q_size=[]

            for _ in range(length):

                node=q.popleft()
                if node:
                    q_size.append(node.val)



                    if node.left:

                        q.append(node.left)

                    if node.right:
                        q.append(node.right)
            if q_size:

                result.append(q_size)

        return result






        