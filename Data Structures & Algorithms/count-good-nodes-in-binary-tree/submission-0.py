# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cur):
            if not node:
                return 0
            if node.val>=cur:
                return dfs(node.left, node.val) + dfs(node.right, node.val) + 1
            else:
                return dfs(node.left, cur) + dfs(node.right, cur)
        return dfs(root, root.val)