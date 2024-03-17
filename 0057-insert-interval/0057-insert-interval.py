class Solution:
    def insert(self, l: List[List[int]], n: List[int]) -> List[List[int]]:
        res=[]
        i=0
        while i<len(l) and n[0]>l[i][1]:
            res.append(l[i])
            i+=1
        while i<len(l) and n[1]>=l[i][0]:
            n[0]=min(n[0],l[i][0])
            n[1]=max(n[1],l[i][1])
            i+=1
        res.append(n)
        while i<len(l):
            res.append(l[i])
            i+=1
        return res