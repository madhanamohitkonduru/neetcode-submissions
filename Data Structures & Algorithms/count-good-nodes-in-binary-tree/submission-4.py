# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = collections.deque()
        q.append([root, root.val])
        while q:
            curr = q.pop()
            currval = curr[0]
            pastmax = curr[1]
            if currval.val>=pastmax:
                res=res+1
            if currval.left:
                q.append([currval.left, max(currval.val, pastmax)])
            if currval.right:
                q.append([currval.right, max(currval.val, pastmax)])

        return res
