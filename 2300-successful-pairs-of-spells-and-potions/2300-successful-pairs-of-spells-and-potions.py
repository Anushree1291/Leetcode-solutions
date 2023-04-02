class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        a=[]
        b=sorted(potions)
        for i in spells:
            c=len(b)-bisect_left(b,math.ceil(success/i))
            a.append(c)
        return a