class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxislands = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def foo(r, c):
            area = 1
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                currrow, currcol=q.popleft()
                for i in directions:
                    newrow = currrow + i[0]
                    newcol = currcol + i[1]
                    if (newrow in range(rows) and newcol in range(cols) and grid[newrow][newcol]==1 and (newrow, newcol) not in visited):
                        q.append((newrow, newcol))
                        visited.add((newrow, newcol))
                        area += 1
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxislands = max(foo(r,c), maxislands)

        return maxislands