class Solution:
    def kidsWithCandies(self, candies: List[int], e: int) -> List[bool]:
        return [i+e>=max(candies) for i in candies]