class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m=len(grid)#cols
        n=len(grid[0])#rows
        q=deque()
        num_fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    num_fresh+=1
        if num_fresh==0:
            return 0
        mins=-1
        while q:
            q_size=len(q)
            mins+=1
            for _ in range(q_size):
                i,j=q.popleft()
                for r,c in[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=r<m and 0<=c<n and grid[r][c]==1:
                        grid[r][c]=2
                        num_fresh-=1
                        q.append((r,c))
        if num_fresh==0:
            return mins
        else:
            return -1
                
