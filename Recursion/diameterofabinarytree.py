#Find the diameter of a binary tree


def inorder(ptr):
    if  ptr:
         inorder(ptr.left)
         print ptr.val
         inorder(ptr.right)   

class treenode:
    def __init__(self,item):
        self.val = item
        self.left = None
        self.right = None
        
#  diameter can be ideally derived by
#1) the diameter of left tree or
#2) the diameter of right tree or
#3) the height of left sub tree + the height of right sub tree + 1 ( 1 to add the root node when the diameter spans across the root node)
        
def recursivediameter(node):
    ldiameter = 0
    rdiameter = 0
    
    if not node:
        return 0
    
   
    lheight = height(node.left)
    rheight = height(node.right)
    ldiameter = 1 + recursivediameter(node.left)
    rdiameter = 1 + recursivediameter(node.right)
    
    return max(ldiameter,rdiameter,lheight+rheight+1)


def height(n):
    if not n:
        return 0
    return 1 + max(height(n.left),height(n.right))
    

    
if __name__ == "__main__":
    #create a sample tree 
    node1 = treenode(10)
    node2 = treenode(11)
    node3 = treenode(15)
    node4 = treenode(16)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    root = node1

    #inorder traversal is called for tetsing purpose
    #inorder(root)

    print 'diameter of tree is %d' % recursivediameter(root)

