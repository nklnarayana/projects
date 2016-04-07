class  Node:
   def __init__(self,item):
      self.data = item
      self.Next = None

class LinkedList:
   def __init__(self):
     self.head = None

   def add(self,item):
     temp = Node(item)
     if self.head == None:
        self.head = temp
        return

     t = self.head
     prev = self.head
     while t != None:
           prev =t
           t = t.Next
     prev.Next = temp


   def printelements(self):
     curr= self.head
     while curr != None:
         print curr.data
         curr = curr.Next

   def reverse(self, head, k):
        current = head 
        next  = None
        prev = None
        count = 0
         
        # Reverse first k nodes of the linked list
        while(current is not None and count < k):
            next = current.Next
            current.Next = prev
            prev = current
            current = next
            count += 1
        
        # next is now a pointer to (k+1)th node
        # recursively call reverse with next as starting list    
        if next is not None:
            #print 'in recursion'
            head.Next = self.reverse(next, k)
        # prev is new head of the input list
         
        return prev     
       
l = LinkedList()
l.add(10)
l.add(20)
l.add(30)

        
l.printelements()

print
#l.head = l.reverse(l.head,2)
l.head = l.reverse(l.head, 2)
print
l.printelements()

