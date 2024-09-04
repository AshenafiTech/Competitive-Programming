# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        def preOrder(node):

            if node:
                # root first
                ans.append(node.val)

                # left node
                preOrder(node.left)

                # right node
                preOrder(node.right)
        preOrder(root)

        return ans
