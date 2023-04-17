import numpy as np
class Solution:
    def kidsWithCandies(self, c: List[int], e: int) -> List[bool]:
        c=np.array(c)
        b=np.max(c);
        d=[]
        for i in c:
            if i+e>=b:
                d.append(True)
            else:
                d.append(False)
        return d