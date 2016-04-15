from collections import deque

class btnode:
   def __init__(self,item):
        self.data = item
        self.left = None
        self.right = None

def buildtree(inor,preor, inStart,inEnd):
   if inStart> inEnd:
      return None
   
   # get current node from preorder traversal and increment preIndex
   node = btnode(preor[buildtree.preIndex])
   buildtree.preIndex += 1
   
   #if the node does not have any children 
   if inStart == inEnd :
          return node     
   #else search for the index of this node in inorder array 
   inIndex = search(inor,inStart,inEnd,node.data)
   

   #using index in inorder traversal construct left and right subtrees
   node.left = buildtree(inor,preor, inStart,inIndex-1)
   node.right = buildtree(inor,preor,inIndex+1,inEnd)
        
   return node  


def search(inor,inStart,inEnd,val):
   for i in range(inStart,inEnd+1):
        if inor[i] == val:
             return i       

#function to print tree
def treeLevels(root):
   # Two queues, one for the nodes one for the level of the nodes.
   Q = deque()
   L = deque()
   #enque the root
   Q.append(root)
   level = 0
   L.append(level)

   print  level,[root.data]


   while len(Q) > 0:
      u = Q.popleft()
      l = L.popleft()
      # For the current node if it has a left or right child,
      # add it to the queue and with its corresponding level + 1.
      if u.left:
           Q.append(u.left)
           L.append(l+1)
      if u.right:
           Q.append(u.right)
           L.append(l+1)

      # If there is a node still in the queue and all the nodes in the queue
      # are at the same level, then increment the level and print.  
      if len(L) > 0 and L[0] > level and L[0] == L[-1]:
          level += 1
          print level,[x.data for x in Q]



if __name__ == "__main__":
   inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']
   preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
   buildtree.preIndex = 0
   
   root = buildtree(inOrder,preOrder,0,len(inOrder)-1)
   treeLevels(root)

