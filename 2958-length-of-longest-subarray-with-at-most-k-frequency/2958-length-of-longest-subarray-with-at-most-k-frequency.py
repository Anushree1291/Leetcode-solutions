from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, n: List[int], k: int) -> int:
        m=defaultdict(int)
        j=0
        ma=0
        for i in range(len(n)):
            m[n[i]]+=1
            while m[n[i]]>k:
                m[n[j]]-=1
                j+=1
            ma=max(ma,i-j+1)
        return ma