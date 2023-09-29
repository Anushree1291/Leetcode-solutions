class Solution:
    def countHillValley(self, n: List[int]) -> int:
        l=n[0]
        c=0
        for i in range(1,len(n)-1):
            if( (l<n[i] and n[i]>n[i+1]) or ( l>n[i] and n[i]<n[i+1])):
                l=n[i]
                c+=1
        
        return c