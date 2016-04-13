class Node:
   def __init__(self,prev,next,key,value):
        self.value = value
        self.prev = prev
        self.next = next
        self.key = key

class Cache:
   def __init__(self,capacity):
        self.top = None
        self.last = None
        self.count = 0
        self.capacity = capacity
        self.key_map ={}

   def is_full(self):
       return  self.count == self.capacity

   def insert(self,key,value):
       
       if self.is_full():
           cache._pop()
                 
       node =  Node(None,self.top,key,value)
       if self.top == None:
           self.top = node
           self.last = node
       else:
           self.top.prev = node
           self.top = node
       # value in ket map is a pointer to the node in double linked list 
       self.key_map[key] = node
       self.count = self.count + 1

   # get the value from existing key_map , delete that node and insert iton top as it has been accessed Least recently 
   def get(self,key):
       node = self.key_map[key]
       self._delete_impl(node)
       self.insert(key,node.value)
       return node.value
   
  
   def set(self,key,value):
       node = self.key_map[key]
       self._delete_impl(node)
       self.insert(key,value)

   def delete(self,key):
       node = self.key_map[key]
       self._delete_impl(node)


   def _delete_impl(self,node):
       #if deleted node is on top or not
       if node.prev is not None:
          node.prev.next = node.next
       else:
          self.top = node.next
       #if deleted node is at bottom of doubly linked list or not
       if node.next is not None:
          node.prev.next = node.next
       else:
          self.last = node.prev
       
       del self.key_map[node.key]
       self.count = self.count - 1

   def _pop(self):
       self._delete_impl(self.last)

   def printdoublelinkedlist(self):
       curr = self.top
       while curr:
           print curr.value,
           curr = curr.next


//create a cahce with capacity of 3 
cache = Cache(3)
cache.insert('lak',115234)
cache.insert('cha',134567)
cache.insert('sam',123456)
print cache.printdoublelinkedlist()
#to test eviction
cache.insert('har',134677)
print cache.printdoublelinkedlist()

print cache.get('cha',)
print cache.printdoublelinkedlist()

cache.set('sam','234567')
print cache.printdoublelinkedlist()



