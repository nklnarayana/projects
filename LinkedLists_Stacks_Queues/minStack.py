#Problem: Implement getMinimim() for a stack. The method returns the minimum element in the entire stack.
# Maintain actual data list and minData list. 

# When pushing element into data list, if  top element in minData is greater than or equal to element to be pushed, then inset element into minData as well. 
# When popping element from data list, if element to be popped is equal to top element in minData , then pop from minData as well 

class Stack:
   def __init__(self):
        self.lst = []
        self.size = 0
        self.minData = []

   def push(self,item):
       self.lst.append(item)
       self.size =  self.size + 1
       print item
       if len(self.minData) == 0:
            self.minData.append(item)
       elif self.minData[-1] >= item :
            self.minData.append(item)

   def pop(self):
       item = self.lst[-1]
       del self.lst[-1]
       self.size =  self.size - 1
       if item ==  self.minData[-1]  : 
             self.minData.pop()
       return  item

   def peek(self):
       return  self.lst[-1]

   def printStack(self):
       print self.lst

   def getMinimum(self):
       return self.minData[-1]


s = Stack()
s.push(20)
s.push(10)
s.push(15)
s.push(10)
print '------'

print s.getMinimum()
s.pop()
print s.getMinimum()



