# This is similar to preorder traversal . Additionaly we store the data of node in an array 
#1. if node.left and node.right is  null(if node is child node),print the array 
#2. if node is not child node node,  then recursively call the function by passing node.left, the array, and its length
#3. if node is not child node node ,then recursively call the function by passing node.right, the array, and its length

class btnode:
   def __init__(self,item):
        self.data = item
        self.left = None
        self.right = None
        
#

def printpaths(node,patharray):
    if node is None:
        return
    
    patharray.append(node.data)
    #pathlen += 1
    
    if node.left is  None and node.right is None:
        printpatharray(patharray)      
    else:
        printpaths(node.left,patharray)
        printpaths(node.right,patharray)
  
def printpatharray(patharray):
    for i in range(0,len(patharray)):
        print patharray[i],
    print
        
if __name__ == "__main__" :
   
   #             100
   #       50          300  
   # 20       70             400
   
   #construct above tree
   root1 = btnode(100)
   root1.left = btnode(50)
   root1.right = btnode(300)
   root1.left.left = btnode(20)
   root1.left.right = btnode(70)
   root1.right.right = btnode(410)

   printpaths(root1,[])

   
