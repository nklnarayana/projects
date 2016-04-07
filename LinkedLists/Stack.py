class Stack:
   def __init__(self):
        self.lst = []
        self.size = 0
      
   def push(self,item):
       self.lst.append(item)
       self.size =  self.size + 1     
           
   def pop(self):
       item = self.lst[-1]
       del self.lst[-1]
       self.size =  self.size - 1    
       return  item
         
   def peek(self):
       return  self.lst[-1]

   def printStack(self):
       print self.lst


s = Stack()

print s.printStack()
s.push(10)
s.push(8)
s.push(7)

print s.printStack()
print 'size of stack is %d' % s.size
s.pop()
print s.printStack()
print 'size of stack is %d' % s.size

