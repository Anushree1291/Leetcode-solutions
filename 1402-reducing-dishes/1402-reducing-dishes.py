class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        s.sort(reverse=True)
        if(s[0]<0):
            return 0
        a=m=s[0]
        for i in range(1, len(s)):
            a+=s[i]
            if m+a<m :
                return m
            m+=a
        return m