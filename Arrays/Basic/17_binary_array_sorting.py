
class Solution:
    # Function to sort the binary array in non-decreasing order
    def binSort(self, arr):
        # code here
        start = 0
        end = len(arr) - 1
        while(start <= end):
            if(arr[start]):
                arr[start], arr[end] = arr[end], arr[start]
                end -= 1
            else :
                start += 1
            



#{ 
 # Driver Code Starts
# Driver code
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    Solution().binSort(arr)  # sort the binary array

    print(*arr)  # print the sorted array
    print("~")

# } Driver Code Ends