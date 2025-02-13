import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n=heapq.heappop(nums)
        c=0
        b=False
        if n<k:
            b=True
        heapq.heappush(nums,n)
        while b:
            a=heapq.heappop(nums)
            b=heapq.heappop(nums)
            heapq.heappush(nums,min(a,b)*2+max(a,b))
            c+=1
            n=heapq.heappop(nums)
            heapq.heappush(nums,n)
            if n>=k or len(nums)<2:
                b=False
            
        return c