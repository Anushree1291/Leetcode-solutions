import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        c=0
        while nums[0]<k:
            n=heapq.heappop(nums)*2+heapq.heappop(nums)
            heapq.heappush(nums,n)
            c+=1
        return c

