class Solution:
    def firstCompleteIndex(self, a: List[int], m: List[List[int]]) -> int:
        s={}
        for i in range(len(a)):
            s[a[i]]=i
        ma=len(a)
        for i in m:
            l=[]
            for j in i:
                l.append(s[j])
            ma=min(ma,max(l))
        for i in range(len(m[0])):
            l=[]
            for j in range(len(m)):
                l.append(s[m[j][i]])
            ma=min(ma,max(l))
        return ma