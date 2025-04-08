#User function Template for python3
class Solution:
    def getAlternates(self, arr):
        # Code Here
        return list(val for i, val in enumerate(arr) if i % 2 == 0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    ls = Solution().getAlternates(arr)
    print(" ".join(map(str, ls)))
    print("~")

# } Driver Code Ends