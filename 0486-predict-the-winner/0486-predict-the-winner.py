class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def tra(left,right):
            if left>right:
                return 0
            
            sumLeft=nums[left]-tra(left+1,right)
            sumRight=nums[right]-tra(left,right-1)
            
            return max(sumLeft,sumRight)
        
        if tra(0,len(nums)-1)>=0:
            return True
        
        return False