class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        m=0
        c=0
        for i in range(0,k):
            if s[i] in "aeiou":
                c+=1
                m=max(m,c)
        
        for i in range(0,len(s)-k+1):
            if s[i] in "aeiou":
                c-=1
                
            if i+k< len(s) and s[i+k] in "aeiou":
                c+=1
                m=max(m,c)
        return m