class Solution:
    
    def isScramble(self, s1: str, s2: str) -> bool:
        mm={}
        if len(s1)!=len(s2):
            return False
        if s1==s2:
            return True
        if len(s1)==1:
            return s1==s2
        
        def tra(s1, s2):
            n=len(s1)
            print(s1, s2, sep=' ')
            if s1==s2:
                mm[s1,s2]=True
                return True
            elif (s1,s2) in mm:
                return mm[s1,s2]
            elif n==1:
                return False
            for i in range (1,len(s1)):
                if (tra(s1[:i],s2[:i])  and  tra(s1[i:],s2[i:])) :
                    mm[s1,s2]=True
                    return True
            
                if (tra(s1[0:i],s2[-i:]) and  tra(s1[i:],s2[0:n-i])) :
                    mm[s1,s2]=True
                    return True
                
            mm[s1,s2]=False
            return mm[s1,s2]
        
        return tra(s1,s2)
        
    
    
                
    
        