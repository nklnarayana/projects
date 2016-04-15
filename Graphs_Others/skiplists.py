import random

class skipnode:
    def __init__(self, height = 0 ,elem = None):
           self.elem = elem 
           self.next = [None] * height
class skiplist:
    def __init__(self):
           self.head = skipnode()

#To search for an element q in a skip list we begin in the topmost level of the header. We go through the list in this level until we find node with the largest element that is smaller than q.

#We then go to the level below and search again for node with the largest element that is smaller than q, but this time we began the search from the node we found in the level above.

#When we find such node, we go down again and repeat this process until we reach the bottom level. The node x found in the bottom level will be the largest element that is smaller than q in the whole list and if q is in this list, it will be to the right of x.

#below function returns a list of nodes in each level that contains the greatest value that is smaller than elem.
    def randomHeight(self):
        return random.randrange(0,33)

    def updateList(self, elem):
     
         update = [None]*len(self.head.next)
         x = self.head
     
         for i in reversed(range(len(self.head.next))):
            while x.next[i] != None and x.next[i].elem < elem:
                x = x.next[i]
                update[i] = x
         
         return update
#The actual find function returns the node corresponding to the query element or None if it is not present in the skip list.
    def find(self,elem,update = None):
         if update == None:
             update = self.updatelist(elem)
         if len(update) > 0 :
             candidate = update[0].next[0]
             if candidate != None and candidate.elem == elem:
                 return candidate
         return None


    def insert(self,elem):
        node = skipnode(self.randomHeight(),elem)
    
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)
   
        update = self.updateList(elem)
        if self.find(elem,update) == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node

    def remove(self,item):
        update = self.updateList(elem)
        x = self.find(elem,update)
        if x != None:
            for i in range(len(x.next)):
                 update[i].next[i] = x.next[i]
                 #if self.head.next[i] == None:
    

sl = skiplist()
sl.insert(24)      
