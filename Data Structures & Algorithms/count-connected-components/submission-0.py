class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = {}

        for u, v in edges:
            dic.setdefault(u, []).append(v)
            dic.setdefault(v, []).append(u)
        
        visited = set()
        ans = 0

        def dfs(cur):
            visited.add(cur)
            if cur in dic:
                for node in dic[cur]:
                    if node not in visited:
                        dfs(node)

        for i in range(n):
            if i in visited:
                continue
            else:
                ans+=1
                dfs(i)
        
        return ans
        