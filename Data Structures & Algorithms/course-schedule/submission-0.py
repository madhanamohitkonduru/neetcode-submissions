class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        maps = dict()
        for i in range(numCourses):
            maps[i]=[]
        for crs, pre in prerequisites:
            maps[crs].append(pre)

        visited= set()

        def dfs(crs):
            if crs in visited:
                return False
            if maps[crs]==[]:
                return True

            visited.add(crs)
            for pre in maps[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            maps[crs]= []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
                