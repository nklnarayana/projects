#This code is not working. largestBST  after returning is appearing as None. Need to debug more on this code.

class  bnode:
    def __init__(self,item):
       self.val = item
       self.left  = None
       self.right = None

def buildbtree():
    node = bnode(10)
    node.left  = bnode(5)
    node.right = bnode(15)
    node.right.left = bnode(6)
    node.right.right = bnode(20)
    node.left.right = bnode(35)

    #return node as root of tree
    return node

def inorder(node):
   if node:
        inorder(node.left)
        print node.val
        inorder(node.right)


def findlargestBST(p,min,max,maxnodes,largestBST,child):
   if not p:
       return 0 

   if min < p.val and p.val< max:
      leftnodes = findlargestBST(p.left,min,p.val,maxnodes,largestBST,child)
      if leftnodes == 0:
            leftchild = None
      else:
            leftchild =child

      rightnodes = findlargestBST(p.right,p.val,max,maxnodes,largestBST,child)
      if rightnodes == 0:
           rightchild = None
      else:
           rightchild = child

      parent = bnode(p.val)
      #print parent.val
      parent.left = leftchild
      parent.right = rightchild
      child = parent
      totalnodes = leftnodes + rightnodes + 1
      if ( totalnodes > maxnodes ) :
           #print 'maxnodes is %d' %maxnodes
           #print 'totalnodes are %d' %totalnodes
           maxnodes = totalnodes
           #print 'here' 
           largestBST = parent
           #print parent.val
           #print largestBST.val
      return totalnodes
   else:
      findlargestBST(p,INT_MIN,INT_MAX,maxnodes,largestBST,child) 
      return 0

 
if __name__ == '__main__':
   root = buildbtree()
   largestBST = None
   child  = None
   global INT_MIN
   global INT_MAX
   INT_MIN = -3200
   INT_MAX = 3200
   maxnodes = INT_MIN
   findlargestBST(root,INT_MIN,INT_MAX,maxnodes,largestBST,child)
   print largestBST.val
   inorder(largestBST)  

      

