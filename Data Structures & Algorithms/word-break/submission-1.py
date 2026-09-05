class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                lw = len(word)

                if i >= lw and s[i-lw:i] == word:
                    dp[i] = dp[i-lw]

                    if dp[i]:
                        break

        return dp[-1]