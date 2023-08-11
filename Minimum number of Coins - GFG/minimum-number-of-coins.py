#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here
        a=[2000,500,200,100,50,20,10,5,2,1]
        c=0
        l=[]
        for i in range(len(a)):
            if N>=a[i]:
                d=N//a[i]
                l.extend([a[i] for _ in range(d)])
                c+=d
                N=N%a[i]
            
        
        
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends