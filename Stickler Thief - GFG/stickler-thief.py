#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        if n==1:
            return a[0]
        elif n==2:
            return max(a[0],a[1])
        elif n==3:
            return max(a[1],a[0]+a[2])
        else:
            a[n-3]+=a[n-1]
            for i in range(n-4,-1,-1):
                a[i]+=max(a[i+2],a[i+3])
            
            return max(a[0],a[1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends