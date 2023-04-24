class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        if(len(s)<len(p)):
            return res
        hm=defaultdict(int)
        
        sl,pl=len(s),len(p)
        
        for ch in p:
            hm[ch]+=1
           
        for i in range(pl-1):
            if s[i] in hm : hm[s[i]]-=1
        
        for i in range(-1,sl-pl+1):
            if i>-1 and s[i] in hm:
                hm[s[i]]+=1
            if i+pl<sl and s[i+pl] in hm:
                hm[s[i+pl]]-=1
            if all(v==0 for v in hm.values()):
                res.append(i+1)
                
                
        return res