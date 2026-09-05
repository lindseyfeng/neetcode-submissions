class Solution:
    def checkValidString(self, s: str) -> bool:
        max_left, min_left = 0, 0

        for c in s:
            if c == "(":
                max_left += 1
                min_left += 1
            elif c == ")":
                max_left -= 1
                min_left -= 1
            else:
                max_left += 1
                min_left -= 1

            if max_left < 0:
                return False

            min_left = max(min_left, 0)

        return min_left == 0