#flip(mirror)  a tree

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


#function to flip a tree
def fliptree(node):
   if node:
       fliptree(node.left)
       fliptree(node.right)
       temp = node.right
       node.right = node.left
       node.left = temp


# function to print value in root and value in it's sibling
def traverse_preorder(root):
   if root:
       print root.val,
       traverse_preorder(root.left)
       traverse_preorder(root.right)

if __name__ == "__main__" :
   #Build tree
   root = buildbtree()
   print 'preorder traversal of a tree before flipping'
   traverse_preorder(root)
   fliptree(root)
   print
   print 'preorder traversal of a tree after flipping'
   traverse_preorder(root)
    
