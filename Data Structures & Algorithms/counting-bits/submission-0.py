class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            res = 0
            for i in range(32):
                if (1 << i) & n:
                    res += 1
            return res
        ans = [0] * (n+1)
        for i in range(n+1):
            ans[i] = count(i)
        return ans


        