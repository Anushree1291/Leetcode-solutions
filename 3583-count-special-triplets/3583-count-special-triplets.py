from collections import defaultdict
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        s= defaultdict(list)
        c=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print(i,j,s)
                if nums[i]==nums[j]*2 :
                    s[j].append(i)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i]*2:
                    for k in s[i]:
                        if k<i:
                            c+=1
                            break
        return c