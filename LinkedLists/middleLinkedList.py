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


   def find(self,item):
      curr = self.head
      while  curr!=None:
          if curr.data == item:
              return True
          else:
             curr = curr.Next
      return False

   def delete(self,item):

      curr = self.head
      prev = self.head
      if curr.data == item:
         self.head = curr.Next
         curr.Next =  None
         return

      while curr !=None:
          if curr.data != item:
               prev = curr
               curr = curr.Next

         else:
              prev.Next = curr.Next
              curr.Next = None
              return

      return '%d is not found in linked list' % item


lkd_lst = LinkedList()
lkd_lst.add(
