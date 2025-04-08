#User function Template for python3
from collections import defaultdict
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        d = defaultdict(int)
        for element in a :
            d[element] += 1
        
        for element in b :
            d[element] -= 1
            if d[element] < 0 :
                return False
        return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        ob = Solution()
        if ob.isSubset(a1, a2):
            print("true")
        else:
            print("false")

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends