#Given a BST with integer values, and a positive (or zero) integer K, print top (smallest)
#K elements from that BST.

class btnode:
     def __init__(self,item):
         self.data = item
         self.left = None
         self.right = None

def traverse_inorder(node,k,couter):
     if node:
         traverse_inorder(node.left,k,counter)
         #based on counter , print the node value
         if counter.data < k:
             print node.data
             counter.data += 1
         else:
             return 
         traverse_inorder(node.right,k,counter)

if __name__ == '__main__':
     #construct a BST
     root = btnode(25)
     root.left = btnode(13)
     root.right = btnode(43)
     root.left.left = btnode(8)
     root.left.right = btnode(17)
     root.right.left = btnode(29)
     root.right.right = btnode(51)
     k = 6
     #counter to store the number of elements printed
     counter = btnode(0)
     #perform inorder traversal 
     traverse_inorder(root,k,counter)
