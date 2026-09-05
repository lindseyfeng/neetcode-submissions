class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]

        for x in nums[1:]:
            prev_max = cur_max
            prev_min = cur_min

            cur_max = max(x, prev_max * x, prev_min * x)
            cur_min = min(x, prev_max * x, prev_min * x)

            ans = max(ans, cur_max)

        return ans