# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,a,n):
        # Your code here
        b=[0]*n
        b[0]=a[0]
        for i in range(1,n):
            b[i]=a[i]+b[i-1]
            
        if b[n-1]==a[n-1]:
            return n
            
        for i in range(n-2,-1,-1):
            a[i]+=a[i+1]
            if a[i]==b[i]:
                return i+1
        
        return -1
            



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends