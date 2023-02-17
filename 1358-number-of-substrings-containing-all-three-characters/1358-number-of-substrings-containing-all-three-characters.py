class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        a,b,c=-1,-1,-1
        
        for i,x in enumerate(s):
            if x == 'a' :
                a = i
            elif x == 'b' :
                b = i
            else :
                c = i
            
            if i>1:
                count += min([a,b,c])+1
                
        return count