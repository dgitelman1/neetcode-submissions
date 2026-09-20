# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(cur):
            if not cur:
                return 0
            nonlocal res
            # we want to compare max path on left side, max path on right side
            # we want to pass up the highest path sum including the current node
            # we also want to maintain res just in case the longest path sum is disjoint
            path_left = dfs(cur.left)
            path_right = dfs(cur.right)
            joined_path = path_left + cur.val + path_right
            path_up = max(path_left + cur.val, path_right + cur.val, cur.val)
            res = max(res, joined_path, path_up)
            return path_up
        dfs(root)
        return res