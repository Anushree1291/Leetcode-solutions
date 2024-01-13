class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a=[0]*26
        for i in s:
            a[ord(i)-ord('a')]+=1
        c=0
        for i in t:
            a[ord(i)-ord('a')]-=1
            if a[ord(i)-ord('a')]<0:
                c+=1
        return c