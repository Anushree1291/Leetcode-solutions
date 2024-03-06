class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        c=0
        s=set()
        for  i in range(len(nums)):
            n=nums[i]
            
            if n%2==0:
                if 2 not in s:
                    c+=1
                    s.add(2)
                while n%2==0:
                    n=n//2


            for j in s:
                if n%j==0:
                    while n%j==0:
                        n=n//j
            
            for j in range(3,int(math.sqrt(n))+1,2):
                if n%j==0:
                    if j not in s:
                        c+=1
                        s.add(j)
                    while n%j==0:
                        n=n//j
            if n>2:
                c+=1
                if n not in s:
                    s.add(n)
        return c