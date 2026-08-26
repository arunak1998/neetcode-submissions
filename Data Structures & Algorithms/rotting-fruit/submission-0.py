class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        rows=len(grid)

        cols=len(grid[0])

        q=deque()

        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=set()


        for r in range (rows):

            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c,0))
                    visited.add((r,c))
        max_time=0
        while q:

            r,c,time=q.popleft()


            max_time = max(max_time, time) 


            for x,y in directions:

                nx=r+x
                ny=c+y

                if 0<=nx<rows and 0<=ny<cols and (nx,ny) not in visited  and grid[nx][ny]==1:
                    grid[nx][ny]=2

                    visited.add((nx,ny))

                    q.append((nx,ny,time+1))
        for r in range(rows):
            for c in range(cols):

                if grid[r][c]==1:
                    return -1

        return max_time



        