class  bnode:
   def __init__(self,item):
     self.val = item
     self.left  = None
     self.right = None

def buildbtree1():
  node1 = bnode(10)
  node2 = bnode(15)
  node3 = bnode(5)
  node4 = bnode(6)
  node5 = bnode(20)

  node1.left  = node3
  node1.right = node2
  node1.right.left = node4
  node1.right.right = node5
  #return node1 as root of tree
  return node1

def buildbtree2():
  node1 = bnode(10)
  node2 = bnode(15)
  node3 = bnode(5)
  node4 = bnode(6)
  node5 = bnode(20)

  node1.left  = node3
  node1.right = node2
  node1.left.right = node4
  node1.right.right = node5
  return node1


# low and high are smallest and largets numbers in binary tree
# I pass low and high to each node. Node's value should be between low and high.
# while doing left recursion  , low remains same , and high is the parents value
# while doing right recursion , high remians same and low is the parent's value
# perform this recursively until leaf node is reached
def isbtreehelper(ptr,low,high):
 if not ptr:
    return True
 if ptr.val > low and ptr.val < high :
     return isbtreehelper(ptr.left, low,ptr.val) and isbtreehelper(ptr.right,ptr.val,high)
 else: 
     return False

def isbtree():
  return isbtreehelper(root,1,100)

if __name__ == "__main__":
   global root
   #build 1st binary tree
   root = buildbtree1()
   #check if 1st binary tree is BST
   print isbtree()
   #build 2nd binary tree
   root = buildbtree2()
   #check if 2nd binary tree is BST
   print isbtree()  

