class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        col = len(grid[0])
        direction = [(0,1), (1,0), (0, -1), (-1, 0)]
        ls = deque()
        visited = 0

        def bfs(ls, visited):
            c=0
            while ls:
                i,j,c = ls.popleft()
                visited+=1
                print(visited, ls)
                for di, dj in direction:
                    if 0 <= di+i < r and 0 <= dj+j < col:
                        if grid[di+i][dj+j] == 1:
                            grid[di+i][dj+j] = -1
                            ls.append((di+i, dj+j, c+1))
            return c, visited
        
        for i in range(r):
            for j in range(col):
                if grid[i][j] ==2:
                    ls.append((i,j,0))
                    visited -=1
                elif grid[i][j] ==1:
                    visited-=1
        
        temp, visited = bfs(ls, visited) 
        return temp if visited  == 0 else -1

        





        