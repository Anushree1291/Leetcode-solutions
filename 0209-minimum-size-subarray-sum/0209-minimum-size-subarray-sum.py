class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        i, j = 0, 0
        c, t = float("inf"), nums[0]
        while j <= len(nums)-1:
            if t < s:
                j += 1
                if j <= len(nums)-1:
                    t += nums[j]
            elif t >= s:
                c = min(j - i + 1, c)
                t -= nums[i]
                i += 1
        return c if c != float("inf") else 0