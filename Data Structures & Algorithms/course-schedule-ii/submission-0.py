from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(numCourses)}   # pre -> courses that need it
        indegree = [0] * numCourses                # number of unfinished prereqs
        output = []

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)

        while q:
            pre = q.popleft()
            output.append(pre)
            for crs in adj[pre]:
                indegree[crs] = indegree[crs] -1
                if indegree[crs] ==0:
                    q.append(crs)
            
        if len(output)==numCourses:
            return output
        else:
            return []