class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])



        q=deque()


        

        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for r in range(rows):
            for c in range(cols):

                if grid[r][c]==0:

                    q.append((r,c,0))



        while q:

            r,c,dist=q.popleft()


            for x,y in directions:
                nx=r+x
                ny=c+y
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 2147483647:  
                    grid[nx][ny] = dist + 1  
                    q.append((nx, ny, dist + 1))







        