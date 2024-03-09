class Solution:
    def resultArray(self, n: List[int]) -> List[int]:
        a1,a2=[n[0]],[n[1]]
        i=2
        while i<len(n):
            if a1[-1]>a2[-1]:
                a1.append(n[i])
            else:
                a2.append(n[i])
            i+=1
        return a1+a2