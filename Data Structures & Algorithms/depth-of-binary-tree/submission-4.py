# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = collections.deque()
        q.append([root, 1])
        max_ht = 0
        while q:
            node, ht = q.pop()
            max_ht = max(ht, max_ht)
            if node.left:
                q.append([node.left, ht+1])
            if node.right:
                q.append([node.right, ht+1])

        return max_ht

        