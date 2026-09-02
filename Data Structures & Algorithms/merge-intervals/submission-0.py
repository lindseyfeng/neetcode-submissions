class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        start, end = intervals[0][0], intervals[0][1]

        for s, e in intervals[1:]:
            if s <= end:
                end = max(e, end)
            else:
                ans.append([start,end])
                start = s
                end = e
        
        ans.append([start, end])
        return ans
