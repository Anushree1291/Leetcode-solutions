import heapq
class Solution:
    def maxKelements(self, n: List[int], k: int) -> int:
        for i in range(len(n)):
            n[i]*=(-1)
        heapq.heapify(n)
        s=0
        while k:
            k-=1
            a=(-1)*heappop(n)
            s+=a
            heappush(n , (math.ceil(a/3))*(-1))
        return s