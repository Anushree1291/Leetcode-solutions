class Solution:
    def intersection(self, n1: List[int], n2: List[int]) -> List[int]:
        l=set()
        i,j=0,0
        n1.sort()
        n2.sort()
        while i<len(n1) and j<len(n2):
            if n1[i]==n2[j]:
                l.add(n1[i])
                i+=1
                j+=1
            elif n1[i]<n2[j]:
                i+=1
            elif n1[i]>n2[j]:
                j+=1
        return list(l)