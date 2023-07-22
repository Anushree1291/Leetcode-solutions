class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        m=collections.defaultdict(list)
        o=0
        
        for i in nums:
            if i==1:
                o+=1
        zl=0
        m[o].append(0)
        ma=o
        for i in range(len(nums)):
            if nums[i]==0:
                zl+=1
            else:
                o-=1
            s=zl+o   
            m[s].append(i+1)
            
            ma=max(ma,s)
            
        #print(m)
        return m[ma]
                
        