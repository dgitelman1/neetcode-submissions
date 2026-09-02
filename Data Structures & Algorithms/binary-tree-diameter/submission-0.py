# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # longest path can be thru the node on both sides or longest path extended
        def helper(root):
            if not root:
                return 0,0
            left, best_left = helper(root.left)
            right, best_right = helper(root.right)
            cur_longest_path = max(best_left, best_right, left+right)
            return max(left, right)+1, cur_longest_path
        return helper(root)[1]