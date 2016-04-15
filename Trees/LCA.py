#Lowest common ancestor in a Binary Tree
class  bnode:
   def __init__(self,item):
     self.val = item
     self.left  = None
     self.right = None

def buildbtree():
  node1 = bnode(10)
  node2 = bnode(15)
  node3 = bnode(5)
  node4 = bnode(6)
  node5 = bnode(20)
  node6 = bnode(35)

  node1.left  = node3
  node1.right = node2
  node1.right.left = node4
  node1.right.right = node5
  node1.left.right = node6 

  #return node1 as root of tree
  return node1

def find_lca(root,val1,val2):
   if root is None:
       return None
   
   #if root has any one of the two values return root
   if root.val == val1 or root.val == val2:
       return root
   #else perform  find_lca on left subtree  and then find_lca on right subtree
   left =  find_lca(root.left,val1,val2)
   right = find_lca(root.right,val1,val2)

   # if both of above functions return NON-NULL, then left tree has one value and right tree has another value 
   # so root is the LCA
   if left and right :
       return  root
   # Otherwise check if left subtree or right subtree is LCA
   if left:
        return left 
   elif right:
       return right  

if __name__ == "__main__" :
    #Build tree
    root = buildbtree()
    val1 = 15
    val2 = 5
    lcanode = find_lca(root,val1,val2)
    print  'lowest common acestor for  %d and  %d is %d' %(val1,val2,lcanode.val)

    val1 = 6
    val2 = 20
    lcanode = find_lca(root,val1,val2)
    print  'lowest common acestor for  %d and  %d is %d' %(val1,val2,lcanode.val)
    
    
    val1 = 6
    val2 = 35
    
    lcanode = find_lca(root,val1,val2)
    print  'lowest common acestor for  %d and  %d is %d' %(val1,val2,lcanode.val)
