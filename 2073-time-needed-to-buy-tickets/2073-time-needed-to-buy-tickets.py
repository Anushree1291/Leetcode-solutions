class Solution:
    def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        a=t[k]
        c=0
        for i in range(len(t)):
            if i<=k:
                if t[i]<a:
                    c+=t[i]
                else: c+=a
            else:
                if t[i]<a:
                    c+=t[i]
                else: c+=a-1
        return c