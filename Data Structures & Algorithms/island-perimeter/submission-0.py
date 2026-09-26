class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = collections.deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.append((i,j))
                    visited.add((i,j))
                    break
            if q:
                break
        peri = 0

        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                newr = r+dr
                newc = c+dc
                if not (newr in range(rows)) or not (newc in range(cols)) or grid[newr][newc]==0:
                    peri = peri+1
                elif (newr,newc) not in visited:
                    q.append((newr, newc))
                    visited.add((newr, newc))
        return peri
        

        

                

