#Create and print a balanced BST from a sorted array
class btnode:
     def __init__(self,item):
         self.data = item
         self.left = None
         self.right = None

def buildbst(srtarr,start,end):
     if start > end:
         return None
     mid = (start+ end )/2
     node = btnode(srtarr[mid])
     node.left = buildbst(srtarr,start,mid-1)
     node.right = buildbst(srtarr,mid+1,end)
     return node

def traverse_inorder(node):
     if node:
         traverse_inorder(node.left)
         print node.data
         traverse_inorder(node.right)      

if __name__ == '__main__':
     srtarr = [8,13,17,25,29]
     root = buildbst(srtarr,0,len(srtarr)-1)
     traverse_inorder(root)

