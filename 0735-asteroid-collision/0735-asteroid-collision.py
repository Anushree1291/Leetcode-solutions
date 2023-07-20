class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        s=[]
        for i in a:
            f=True
            while len(s)>0 and s[-1]>0 and i<0:
                if abs(s[-1])<abs(i):
                    s.pop()
                    continue
                elif abs(s[-1])==abs(i):
                    s.pop()
                f=False
                break
            if f:
                s.append(i)
        return s