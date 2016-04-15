#problem: Given K sorted arrays of size N each,merge them and print the sorted output. Assume N is very large compared  to K. N may not even be known. i.e. the arrays could be just sorted streams, e.g.timestamp streams.
# I used linked lists for inputs instead of arrays 
import heapq    
def mergeklists(lists):
    ret, heap = [],[] 
    for lst in lists:
           curr = lst.head 
           #push elements of each list into a heapq
           #this makes sure that min element is the root of the tree
           while curr:
               heapq.heappush(heap,curr.data)
               curr = curr.Next 
    # pop the top element of heap and append it to merged array.
    # perform this until there are elements in heap.each time min element of remaining set would be fetched and appended to merged array
    while heap:
        ret.append(heapq.heappop(heap)) 
    return ret
class Node:
    def __init__(self,item):
        self.data= item 
        self.Next = None
class List:
    def __init__(self):
        self.head = None
    def add(self,item):
        temp = Node(item)
        if self.head == None :
            self.head = temp
            return

        curr = self.head 
        prev = curr
        while curr != None:
            prev = curr
            curr = curr.Next
        prev.Next = temp 
        return
    def printelem(self): 
        curr = self.head 
        while curr != None:
            print curr.data, 
            curr = curr.Next
l1= List() 
l1.add(2) 
l1.add(5) 
l1.add(16) 
l1.add(23)

l2= List() 
l2.add(3) 
l2.add(7) 
l2.add(9) 
l2.add(36)

l3= List() 
l3.add(4) 
l3.add(9)
l3.add(11) 
l3.add(67)


print 'first array:', l1.printelem() 
print
print 'second array:',l2.printelem()
print
print 'thrid array:',l3.printelem()
print
#call mergeklists
print 'merged array', mergeklists([l1,l2,l3])
