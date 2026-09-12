class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        island=0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row,col =q.popleft()
                for i in directions:
                    nr = row + i[0]
                    nc = col + i[1]
                    if (nr in range(rows) and nc in range (cols) and (nr, nc) not in visited and grid[nr][nc]=="1"):
                        q.append((nr, nc))
                        visited.add((nr,nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r, c) not in visited:
                    bfs(r,c)
                    island = island + 1

        return island