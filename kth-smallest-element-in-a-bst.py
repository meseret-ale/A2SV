# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        vals = []
        def helper(node):
            nonlocal vals
            if node == None:
                return 0

            helper(node.left)
            helper(node.right)
            vals.append(node.val)
            
        helper(root)
        vals.sort()
        return vals[k-1]