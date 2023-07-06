#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        # base case
        if low >= high:
            return

        # partition logic
        p = self.partition(arr, low, high)

        # recursion call
        self.quickSort(arr, low, p - 1)
        self.quickSort(arr, p + 1, high)
    
    def partition(self,arr,low,high):
        # code here
        # choose pivotElement
        pivotIndex = low
        pivotElement = arr[low]

        # place at right position
        count = 0
        for i in range(low + 1, high + 1):
            if arr[i] <= pivotElement:
                count += 1
        rightIndex = low + count
        arr[pivotIndex], arr[rightIndex] = arr[rightIndex], arr[pivotIndex]
        pivotIndex = rightIndex

        # left smaller element and right bigger element
        i, j = low, high
        while i < pivotIndex and j > pivotIndex:
            while arr[i] <= arr[pivotIndex]:
                i += 1
            while arr[j] > arr[pivotIndex]:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        return pivotIndex
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends