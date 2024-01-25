class Solution:
    def minimumPushes(self, w: str) -> int:
        l=len(w)
        return (l+max(0,l-8)+max(0,l-16)+max(0,l-24)+max(0,l-26))