# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        output = []
        while queue:
            cur, depth = queue.popleft()
            if depth>=len(output):
                output.append([])
            output[depth].append(cur.val)
            if cur.left:
                queue.append((cur.left, depth+1))
            if cur.right:
                queue.append((cur.right, depth+1))
        return output
