class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        s=0;
        for i in nums:
            s+=i
            a.append(s)
        return a