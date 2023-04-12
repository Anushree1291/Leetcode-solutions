class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        k={}
        for i in range(len(s)):
            if( (s[i]  in k) and k.get(s[i])!=t[i]):
                return False
            elif( s[i] not in k  and (t[i]  in k.values())):
                return False
            else:
                k[s[i]]=t[i]
            
        return True