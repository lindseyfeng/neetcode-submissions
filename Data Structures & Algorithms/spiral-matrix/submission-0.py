class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dic = {
            (0,1):(1,0),
            (1,0):(0,-1),
            (0,-1):(-1,0), 
            (-1,0):(0,1)
        }
    
        di, dj = 0, 1
        i, j = 0, 0

        r = len(matrix)
        col = len(matrix[0])
        
        ans = []
        visited = set()

        while len(ans) < r * col:
            ans.append(matrix[i][j])
            visited.add((i, j))

            ni = i + di
            nj = j + dj

            if (
                0 <= ni < r
                and 0 <= nj < col
                and (ni, nj) not in visited
            ):
                i, j = ni, nj
            else:
                di, dj = dic[(di, dj)]
                i += di
                j += dj
        
        return ans