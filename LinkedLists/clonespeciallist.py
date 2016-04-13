
#You are given a Double Link List with one pointer of each node pointing to the next node just like in a single link list. The second pointer however CAN point to any node in the list and not just the previous node. Now write a program in O(n) time to duplicate this list. That is, write a program which will create a copy of this list.

#Let us call the second pointer as arbit pointer as it can point to any arbitrary node in the linked list.


class randomnode:
    def __init__(self,item):
        self.val = item
        self.next = None
        self.random = None

def printelements(LkList):
    curr = LkList
    while curr:
        print curr.val,
        curr = curr.next
    print    
                

if __name__ ==  "__main__":
    
    node1 = randomnode(10)
    node2 = randomnode(20)
    node3 = randomnode(30)
    node1.next = node2
    node2.next = node3
    node1.random = node3
    node2.random = node1
    node3.random = node2
    head = node1
    
    printelements(head)
    
    curr = head
    # copy each node and insert it between it and the next node
    while curr:
        temp = randomnode(curr.val)
        temp.data = curr.val
        
        #inserting into original list
        temp.next = curr.next
        curr.next = temp
        curr = curr.next.next
        
 
        
    # assign random pointers to copy list     
    curr = head
    while curr:
        if curr.random == None:
             curr.next.random = None
        curr.next.random = curr.random.next
        curr = curr.next.next

    
    dummy = randomnode(0)
    copy_current = dummy
    current = head
    while current:
        copy_current.next = current.next
        current.next = current.next.next
        copy_current,current = copy_current.next,current.next
     
    #print original list    
    printelements(head)
    #print copy list
    printelements(dummy.next)
        
