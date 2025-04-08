# Your task is to complete this function
# Function should return true/false
def palindrome(num) :
    n = num
    temp = 0
    while(num) :
        temp = temp * 10 +  num % 10
        num = int(num / 10)
    # print(temp, n)
    return temp == n
def isPalinArray(arr):
    # Code here
    for num in arr :
        if not palindrome(num) :
            return False
    return True



#{ 
 # Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if isPalinArray(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends