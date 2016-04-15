
#class for doubly linked list
class dlnode:
  def __init__(self,item):
      self.val =item
      self.prev = None
      self.next = None

#class for binary tree node
class bnode:
  def __init__(self,item):
      self.val =item
      self.left = None
      self.right = None

class circulardoublybllist:
     #initialize tail and head to None
     def __init__(self):
         self.head =None
         self.tail = None

     # add a node in doubly linked list
     def add(self,item):
         curr = self.head
         temp = dlnode(item)
         if curr is None:
            self.head = temp
            return
 
         while curr:
           previous = curr
           curr = curr.next

         #connect  prev and temp nodes with prev and next pointers
         previous.next= temp
         temp.prev = previous
         self.tail = temp
         
 
     def printelements(self):
         
         curr = self.head 
         temp = curr
         while curr :
            print curr.val
            curr = curr.next
            # since it is a circular doubly linked list, each time value of curr node needs to be compared to value of head node 
            # and if both are same, it means we finished traversing the circular doubly linked list once. 
            if curr.val == temp.val:
                break
    # make the next pinter of last node to point to head of the doubly linked list. 
    # and make the prev of head node to point to tail of doubly linked list 
     def makecircluar(self):
         self.tail.next= self.head
         self.head.prev = self.tail
        

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

#perform inorder traversal of BST  so that numbers are in ascending order
def bsttocrcdbllst(node):
 
     if node is None: return 
     bsttocrcdbllst(node.left)
     #call add method of circluar linked list to add the root node.    
     crcdbllst.add(node.val)
     bsttocrcdbllst(node.right)  
     return crcdbllst 


if __name__ == '__main__':

    root = buildbtree()
    crcdbllst = circulardoublybllist()

    #construct the doubly linked list in ascending order
    bsttocrcdbllst(root)
    
    # make the doubly linked list circular
    crcdbllst.makecircluar()   
    crcdbllst.printelements() 
    
     
