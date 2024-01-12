class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        c1,c2=0,0
        for i in range(0,len(s)//2):
            c=s[i]
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
                c1+=1
            c=s[i+len(s)//2]
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
                c2+=1
        return c1==c2