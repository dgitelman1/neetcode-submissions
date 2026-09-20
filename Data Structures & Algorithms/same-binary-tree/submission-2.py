# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (q and not p):
            return False
        if not (p and q):
            return True
        queue_1 = deque([p])
        queue_2 = deque([q])
        while queue_1 and queue_2:
            node_1 = queue_1.popleft()
            node_2 = queue_2.popleft()
            if node_1.val!=node_2.val:
                return False
            if (node_1.left and not node_2.left) or (node_2.left and not node_1.left):
                return False
            if (node_1.right and not node_2.right) or (node_2.right and not node_1.right):
                return False
            if node_1.left and node_2.left:
                queue_1.append(node_1.left)
                queue_2.append(node_2.left)
            if node_1.right and node_2.right:
                queue_1.append(node_1.right)
                queue_2.append(node_2.right)
        return queue_1==queue_2