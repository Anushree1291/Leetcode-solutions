#User function Template for python3

class Solution:
    def setSetBit(self, x, y, l, r):
        b_y = list("{:032b}".format(y))
        b_x = list("{:032b}".format(x))
        for i in range(32-r,33-l):
            if b_y[i] == '1':
                b_x[i] = '1'
        res = "".join(b_x)
        return(int(res,2))



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        x = int(arr[0])
        y = int(arr[1])
        l = int(arr[2])
        r = int(arr[3])
        
        ob = Solution()
        print(ob.setSetBit(x, y, l, r))
# } Driver Code Ends