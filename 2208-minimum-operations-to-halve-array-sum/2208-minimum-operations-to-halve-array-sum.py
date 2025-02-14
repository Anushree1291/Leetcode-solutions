import heapq
class Solution:
    def halveArray(self, num: List[int]) -> int:
        s=sum(num)
        st=s
        c=0
        for i in range(len(num)):
            num[i]*=(-1)
        heapq.heapify(num)
        while s-st<s/2:
            n=(-1)*heapq.heappop(num)
            st=st-n+n/2
            heapq.heappush(num,(-1)*(n/2))
            c+=1
        return c