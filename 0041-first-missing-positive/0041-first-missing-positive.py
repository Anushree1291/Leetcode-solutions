class Solution:
    def firstMissingPositive(self, n: List[int]) -> int:
        a=[0]*(len(n)+1)
        for i in n:
            if(i>0 and i<=len(n)):
                a[i-1]=1
        #print(a)
        for i in range(len(a)):
            if(a[i]==0):
                return i+1
        return -1
        