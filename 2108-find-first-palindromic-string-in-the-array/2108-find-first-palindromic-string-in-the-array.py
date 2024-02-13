class Solution:
    def firstPalindrome(self, w: List[str]) -> str:
        

        def tra(s):

            b=True
            for i in range(len(s)//2):
                if s[i]!=s[len(s)-i-1]:
                    return False
            return True
        

        for i in w:
            if tra(i):
                return i
        return ""