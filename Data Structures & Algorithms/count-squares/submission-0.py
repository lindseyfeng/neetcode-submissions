class CountSquares:

    def __init__(self):
        self.dic = {}

    def add(self, point: List[int]) -> None:
        p = tuple(point)
        self.dic[p] = self.dic.get(p, 0) + 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0

        for (x2, y2), cnt in self.dic.items():
            if abs(x2 - x) != abs(y2 - y) or x2 == x:
                continue

            ans += (
                cnt
                * self.dic.get((x2, y), 0)
                * self.dic.get((x, y2), 0)
            )

        return ans