class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = Counter(nums)
        arr = sorted(c.items(), key=lambda x: x[1], reverse=True)

        return arr[0][0]
