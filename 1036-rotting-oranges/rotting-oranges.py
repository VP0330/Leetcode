class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        fresh=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
        if fresh==0:
            return 0
        min_time=-1
        while q:
            q_size=len(q)
            min_time+=1
            for _ in range(q_size):
                i,j = q.popleft()
                for r,c in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
                    if 0<=r<rows and 0<=c<cols and grid[r][c]==1:
                        grid[r][c]=2
                        fresh-=1
                        q.append((r,c))
        if fresh==0:
            return min_time
        else:
            return -1