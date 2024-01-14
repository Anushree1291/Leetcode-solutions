class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        l=[i for i in range(len(s)) if s.startswith(a,i)]
        m=[i for i in range(len(s)) if s.startswith(b,i)]
        res=[]
        for i in l:
            for j in m:
                if abs(i-j)<=k:
                    res.append(i)
                    break
        return res