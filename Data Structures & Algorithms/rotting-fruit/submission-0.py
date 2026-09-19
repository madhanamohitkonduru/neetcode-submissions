class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        s = set()
        q = collections.deque()

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        curr_pos = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([(r, c), 0])
                    s.add((r,c))

        while q:

            curr= q.popleft()
            curr_row, curr_col = curr[0]
            curr_pos = curr[1]

            for r, c in directions:
                new_row = curr_row + r
                new_col = curr_col + c

                if (new_row in range(rows) and new_col in range(cols) and (new_row, new_col) not in s and grid[new_row][new_col]!=0):
                    q.append([(new_row, new_col), curr_pos+1])
                    s.add((new_row, new_col))
                    grid[new_row][new_col] = 2

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return curr_pos