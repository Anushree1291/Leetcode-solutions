class Solution:
    def rearrangeArray(self, n: List[int]) -> List[int]:
        q=[]
        p=[]
        for i in n:
            if i<0:
                q.append(i)
            else:
                p.append(i)
        for i in range(len(n)):
            if i%2==0:
                n[i]=p.pop(0)
            else:
                n[i]=q.pop(0)
        return n