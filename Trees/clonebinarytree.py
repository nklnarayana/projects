# Make a copy of a binary tree given pointer to it's root node

#class for binary tree node
class bnode:
  def __init__(self,item):
      self.val =item
      self.left = None
      self.right = None


def buildbtree():
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

#function to clone binary tree
# perform preorder traversal as it first gets root of tree and construction a tree in this traversal is easy.
def clonebinarytree(root):
     node = None
     if root is not None:
          node = bnode(root.val)
          node.left = clonebinarytree(root.left)
          node.right = clonebinarytree(root.right)
     return node

def preorder(root):
    if root:
       print root.val,
       preorder(root.left)
       preorder(root.right)


if __name__ == '__main__':

    root = buildbtree()
    print 'preorder traversal of original binary tree' 
    preorder(root)
    print    
    #clone the binary tree by calling cloneninarytree function which returns head of cloned binary tree
    clonehead= clonebinarytree(root)
    print 'preorder traversal of cloned  binary tree'
    preorder(clonehead)
    



