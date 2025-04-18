#User function Template for python3


'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque as dq
class Solution:
    #Function to return a list containing the postorder traversal of the tree.
    # using stack for efficient use of heap
    # def postOrder(self, root):
    #     stack = dq()
    #     res = []
    #     if root:
    #         stack.append(root)
    #     else :
    #         return res
    #     while(stack):
    #         top = stack.pop()
    #         res.append(top.data)
    #         if top.left:
    #             stack.append(top.left)
    #         if top.right:
    #             stack.append(top.right)
    #     res.reverse()
    #     return res
        # code here
        
    # using recursion
    def postOrder(self, root):
        res = []
        if not root:
            return res
        res += self.postOrder(root.left)
        res += self.postOrder(root.right)
        res.append(root.data)
        return res
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    #Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        res = ob.postOrder(root)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

        print("~")

# } Driver Code Ends