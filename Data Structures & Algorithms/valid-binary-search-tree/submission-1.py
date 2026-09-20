# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur, min_val, max_val):
            if not cur:
                return True
            if not (min_val < cur.val < max_val):
                return False
            return dfs(cur.left, min_val, cur.val) and dfs(cur.right, cur.val, max_val)

        return dfs(root, float('-inf'), float('inf'))