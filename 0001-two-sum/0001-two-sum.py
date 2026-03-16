class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for k,v in enumerate (nums):
            if v in s:
                return [ k , s.get(v)]
            else:
                s[target - v] = k

