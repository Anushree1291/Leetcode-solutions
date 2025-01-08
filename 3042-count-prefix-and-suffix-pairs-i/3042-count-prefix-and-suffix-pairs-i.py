class Solution:
    def countPrefixSuffixPairs(self, w: List[str]) -> int:
        c=0
        for i in range(len(w)):
            l=len(w[i])
            for j in range(i+1,len(w)):
                #print(w[i], w[j], w[j][:l], w[j][-l:])
                if w[j][:l]==w[i] and w[j][-l:]== w[i] :
                    c+=1
        return c