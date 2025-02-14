class Solution:
    def findIntersectionValues(self, n1: List[int], n2: List[int]) -> List[int]:
        a1,a2=0,0
        for i in n1:
            if i in n2:
                a1+=1
        for i in n2:
            if i in n1:
                a2+=1
        return [a1,a2]