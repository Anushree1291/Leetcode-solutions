class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        m=defaultdict(list)
        r=[0]*len(nums)
        for i in range(len(nums)):
            m[nums[i]].append(i)
        for l in m.values():
            s=0
            p=0
            for i in l:
                s+=i
            for i in range(len(l)):
                r[l[i]]=s - l[i] * (len(l) - i) + l[i] * i - p
                p=p+l[i]
                s=s-l[i]
        return r