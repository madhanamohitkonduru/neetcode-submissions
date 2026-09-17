# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append([root,1])
        while q:
            popped = q.pop()
            if popped[0]:
                res.append([popped[0].val, popped[1]])
                if popped[0].left:
                    q.append([popped[0].left, popped[1]+1])
                if popped[0].right:
                    q.append([popped[0].right, popped[1]+1])
        s = set()
        r = []
        for i,j in res:
            if j in s:
                continue
            else:
                s.add(j)
                r.append(i)

        return r
