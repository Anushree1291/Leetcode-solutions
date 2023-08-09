class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        a.sort()
        m=10000000
        for i in range(len(a)-1):
            m=min(m,a[i+1]-a[i])
        
        l=[]
        
        for i in range(len(a)-1):
            if a[i+1]-a[i] ==m:
                l.append([a[i],a[i+1]])
        return l