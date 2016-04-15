# A binary search tree problem  Populating next right pointers in each node

#class for binary tree node
class bnode:
  def __init__(self,item):
      self.val =item
      self.left = None
      self.right = None
      self.sibling = None


def buildbtree():
      node1 = bnode(10)
      node1.left  = bnode(5)
      node1.right = bnode(15)
      node1.left.left = bnode(2)
      node1.left.right = bnode(6)
      node1.right.left = bnode(13)
      node1.right.right = bnode(20)
     
      return node1

# Traverse the tree in inorder
# connect sibling of left child to nodes' right child only when left child exist
# connect sibling of right child to nodes' siblings' left child . if nodes' sibling is None, then sibling of right child is None


def findsiblingptr(node):
      if not node: 
          return 
      if node.left:
            node.left.sibling = node.right
      if node.right and node.sibling:
            node.right.sibling = node.sibling.left
      elif node.right:
            node.right.sibling = None
   
      findsiblingptr(node.left)      
      findsiblingptr(node.right)
    
# function to print value in root and value in it's sibling
def traverse_preorder(root):
      if root:
            print root.val,
            if root.sibling:
                 print root.sibling.val ,
            else:
                 print None,
            traverse_preorder(root.left)
            traverse_preorder(root.right)

if __name__ == '__main__':
      #build binary search tree
      root = buildbtree()
      #call the fuinction to assign sibling pointer
      findsiblingptr(root)
      # call traverse preorder to print the nodes' value and sibling's value
      traverse_preorder(root)
    
