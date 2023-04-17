class Solution:
    def kidsWithCandies(self, candies: List[int], e: int) -> List[bool]:
        x=max(candies)
        return [i+e>=x for i in candies]