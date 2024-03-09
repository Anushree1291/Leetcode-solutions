class Solution:
    def getCommon(self, n1: List[int], n2: List[int]) -> int:
        i,j=0,0
        while i<len(n1) and j <len(n2):
            if n1[i]==n2[j]:
                return n1[i]
            elif n1[i]<n2[j]:
                i+=1
            elif n1[i]>n2[j]:
                j+=1
        return -1