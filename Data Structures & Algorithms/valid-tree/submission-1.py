class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        dic = {}

        for u, v in edges:
            dic.setdefault(u, []).append(v)
            dic.setdefault(v, []).append(u)

        def dfs(cur, parent):
            if cur in visited:
                return False

            visited.add(cur)

            for node in dic.get(cur, []):
                if node == parent:
                    continue

                if not dfs(node, cur):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n