class Solution:
    def reverseVowels(self, s: str) -> str:
        a=[]
        b=0
        for ch in s:
            if ch in "aeiouAEIOU":
                a.append(ch)
                b+=1
        st=""
        b-=1
        for ch in s:
            if ch in "aeiouAEIOU":
                st+=a[b]
                b-=1
            else:
                st+=ch
        return st
                