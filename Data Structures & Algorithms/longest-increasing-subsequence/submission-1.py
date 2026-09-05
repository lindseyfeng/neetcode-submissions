from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        new_nums = [nums[0]]

        for x in nums[1:]:
            idx = bisect_left(new_nums, x)

            if idx == len(new_nums):
                new_nums.append(x)
            else:
                new_nums[idx] = x

        return len(new_nums)