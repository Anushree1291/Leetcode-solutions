class Solution:
    def divisorGame(self, n: int) -> bool:
        if n==1:
            return False
        if n%2==0:
            return True
        return False