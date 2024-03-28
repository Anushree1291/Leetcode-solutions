class Solution:
    def maxSubarrayLength(self, n: List[int], k: int) -> int:
        m={}
        i,j=0,0
        ma=0
        while i<len(n):
            if n[i] not in m:
                m[n[i]]=1
            else:
                m[n[i]]+=1
            if m[n[i]]>k:
                ma=max(ma,i-j)
                while m[n[i]]>k:
                    m[n[j]]-=1
                    j+=1
            i+=1
            ma=max(ma,i-j)

            
        return ma