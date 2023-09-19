class Solution:
    def findDuplicate(self, n: List[int]) -> int:
        a=[0]*(len(n)+1)
        for i in n:
            a[i]+=1
            if a[i]==2:
                return i
        return 0