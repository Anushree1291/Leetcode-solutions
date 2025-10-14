class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k ==1:
            return True
        s=set()
        for i in range(len(nums)-k+1):
            print("i : ", i)
            f=True
            for j in range(i,i+k-1):
                print("j : ", j, j+1)
                if nums[j+1]<= nums[j]:
                    f=False
                    break
            if f:
                if i-k in s:
                    return True
                print(i)
                s.add(i)
        print(s)
        return False