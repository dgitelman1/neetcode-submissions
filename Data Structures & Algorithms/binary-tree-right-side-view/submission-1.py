# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return output
        queue = deque([(root, 0)])
        while queue:
            cur, depth = queue.popleft()
            if depth>=len(output):
                output.append(cur.val)
            else:
                output[depth] = cur.val
            if cur.left:
                queue.append([cur.left, depth+1])
            if cur.right:
                queue.append([cur.right, depth+1])
        return output