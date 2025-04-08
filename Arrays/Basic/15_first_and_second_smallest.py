#User function Template for python3
class Solution:
    def minAnd2ndMin(self, arr):
        #code here
        smallest = arr[0]
        second_smallest = -1
        for val in arr:
            if val < smallest :
                second_smallest = smallest
                smallest = val
            elif(val != smallest) :
                if second_smallest == -1:
                    second_smallest = val
                elif val < second_smallest:
                    second_smallest = val
        if second_smallest == -1 :
            return [-1]
        else: 
            return [smallest, second_smallest]
                
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        product = obj.minAnd2ndMin(arr)
        if product[0] == -1:
            print(product[0])
        else:
            print(product[0], end=" ")
            print(product[1])

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends