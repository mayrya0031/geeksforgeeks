#User function Template for python3

class Solution:
    def rotate(self, arr):
        n = len(arr)
        arr[:n - 1] = arr[:n - 1][::-1]
        arr[:] = arr[::-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rotate(arr)
        print(" ".join(map(str, arr)))
        print("~")
        t -= 1

# } Driver Code Ends