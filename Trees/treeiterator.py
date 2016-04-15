#Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#Calling next() will return the next smallest number in the BST.
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

class  bnode:
   def __init__(self,item):
     self.val = item
     self.left  = None
     self.right = None

class treeiterator():
     def __init__(self,root):
          self.stack = []
          self.pushall(root)
     # while initilaizing the iterator, push all elemenst from root to last node in left subtree 
     # due to this root will be at bottom and min node will be on top of stack
     def pushall(self,node):
          while node:
              self.stack.append(node)
              node = node.left
     #to get next (min value) , pop from stack and then perform pushall for the right node of the node that is popped
     def next(self):
         tempnode = self.stack.pop()
         self.pushall(tempnode.right)
         return tempnode.val
    
     def hasnext(self):
         return not len(self.stack) == 0

 
               
def buildbtree():
  node1 = bnode(10)
  node1.left  = bnode(7)
  node1.right = bnode(17)
  node1.right.left = bnode(13)
  node1.right.right = bnode(20)
  #return node1 as root of tree
  return node1
 

if __name__ == '__main__':
     root = buildbtree()
     treeiter = treeiterator(root)
     
     while True:
        print treeiter.next()
        hasnext= treeiter.hasnext()
        print hasnext
        if hasnext == False : break



     
