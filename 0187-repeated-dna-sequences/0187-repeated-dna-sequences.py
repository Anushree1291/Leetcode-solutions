class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        li=[]
        if len(s)<10:
            return li
        l={}
        for i in range(len(s)-9):
            su=s[i:i+10]
            if su not in l:
                l[su]=0
            elif su not in li:
                li.append(su)
                
        return li