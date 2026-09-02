class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        r = len(grid)
        c = len(grid[0])

        q = deque()

        # 所有 treasure 一起作为 BFS 起点
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.popleft()

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if (
                    0 <= ni < r
                    and 0 <= nj < c
                    and grid[ni][nj] == 2147483647
                ):
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni, nj))