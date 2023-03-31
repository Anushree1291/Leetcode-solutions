class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        m={}
        for ind,i in enumerate(nums):
            if i in m:
                return [ind,m[i]]
            else:
                m[t-i]=ind
                
        return []