class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [ [0,1],[0,-1],[1,0], [-1,0]]
        mainset=set()

        def bfs(r,c):
            defset = set()
            q = collections.deque()
            defset.add((r,c))
            mainset.add((r,c))
            q.append((r,c))
            flag = False

            while q:
                r, c = q.popleft()
                for dr,dc in directions:
                    newr = r+dr
                    newc = c+dc
                    if ((newr in range(rows)) and (newc in range(cols)) and (board[newr][newc]=="O") and ((newr, newc) not in defset)):
                        defset.add((newr, newc))
                        mainset.add((newr, newc))
                        q.append((newr, newc))

            for r,c in defset:
                if r==0 or r==rows-1 or c ==0 or c==cols-1:
                    flag=True
                    break

            if flag==False:
                for r,c in defset:
                    board[r][c]="X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and (r,c) not in mainset:
                    bfs(r,c)