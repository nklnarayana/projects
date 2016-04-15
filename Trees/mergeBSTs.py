#1) Do inorder traversal of first tree and store the traversal in one temp array arr1[]. This step takes O(n1) time.
#2) Do inorder traversal of second tree and store the traversal in another temp array arr2[]. This step takes O(n2) time.
#3) The arrays created in step 1 and 2 are sorted arrays sicne they are BSTs. Merge the two sorted arrays into one array of size n1 + n2. This step takes O(n1+n2) time.
#4) Construct a balanced tree from the merged array using merge sort (excep splliting the list). This step takes O(n1+n2) time.

#Time complexity of this method is O(n1+n2)

from collections import deque

#create binary tree node class 
class btnode:
   def __init__(self,item):
        self.data = item
        self.left = None
        self.right = None


#Do an inorder traversal 
#append the root's data to an array
def storeInorder(node,inorder):
   if node == None:
       return 
   storeInorder(node.left,inorder)
   inorder.append( node.data)
   #index_ptr += 1
   storeInorder(node.right,inorder)

#merge two arrays
def merge(arr1,arr2):
   m = len(arr1)
   n = len(arr2)
   mergedArr = [None] * ( m + n )
   i = 0
   j = 0
   k = 0
   
   # traverse through each array until their ends
   while i < m and j < n:
      # Idea is to find which element is small compared to two numbers in arr1 & arr2
      # Assign the smalles number to mergesArr 

      # if arra1 element is small
      if arr1[i] < arr2[j]:
           mergedArr[k] = arr1[i]
           i += 1
      #if arr2 element is small
      else: 
           mergedArr[k] = arr2[j]
           j += 1
      
      k += 1

  
  # scan the remainining elements in each array and append them to mergedArray 
   while i < m:
      mergedArr[k] = arr1[i]
      i += 1     
      k += 1  
   
   while j < n:
      mergedArr[k] = arr1[j]   
      j += 1
      k += 1

   return mergedArr

#function to construct BST from a sorted list
def sortedArraytoBST(arr,start,end):
  
   if start> end :
      return None

   mid = (start + end ) / 2
   #make mid element as root to keep search tree balanced
   root =  btnode(arr[mid]) 
   #recursively construct left subtree and assign as left node of root
   root.left = sortedArraytoBST(arr,start,mid-1)
   #recirsively construct right subtree and assign it as right node of root
   root.right = sortedArraytoBST(arr,mid+1,end)
   return root

def printInorder(node):

   if node is None:
      return 

   printInorder(node.left)
   print node.data,
   printInorder(node.right)  

def treeLevels(root):
   # Two queues, one for the nodes one for the level of the nodes.
   Q = deque()
   L = deque()
   #enque the root
   Q.append(root)
   level = 0 
   L.append(level)
   
   print level, [root.data]
   

   while len(Q) > 0:
      u = Q.popleft()
      l = L.popleft()
      # For the current node if it has a left or right child,
      # add it to the queue and with its corresponding level + 1.
      if u.left:
           Q.append(u.left)
           L.append(l+1)
      if u.right:
           Q.append(u.right)
           L.append(l+1)
      
      # If there is a node still in the queue and all the nodes in the queue
      # are at the same level, then increment the level and print.  
      if len(L) > 0 and L[0] > level and L[0] == L[-1]:
          level += 1
          print level,[x.data for x in Q]


if __name__ == "__main__" :
   root1 = btnode(100)
   root1.left = btnode(50)
   root1.right = btnode(300)
   root1.left.left = btnode(20)
   root1.left.right = btnode(70)

   root2 = btnode(80)
   root2.left = btnode(40)
   root2.right = btnode(120)

   inorder1 = []
   inorder2 = []   
   # storeInorder traversals of the trees in inorder1 and inorder2

   storeInorder(root1,inorder1)
   storeInorder(root2,inorder2)

   mergedArr = merge(inorder1,inorder2)
   
   start =0
   end = len(mergedArr)-1
   # construct Binary search tree from sorted merged array
   root = sortedArraytoBST(mergedArr,0,end)
   
   printInorder(root) 
   print
   treeLevels(root)  
