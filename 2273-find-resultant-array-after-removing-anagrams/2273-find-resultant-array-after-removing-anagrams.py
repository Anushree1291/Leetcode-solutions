from collections import Counter
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        final=[words[0]]
        for i in range(1,len(words)):
            if sorted(words[i])  != sorted(words[i-1]):
                final.append(words[i])
        return final