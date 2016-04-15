# Build a max heap of size k.
# Scan remaining elements and if element is less than root , replace root with that element and heapify thr root
# remaining elements are nearest points to p.
# Make sure the code modifies same list during fucntions passes

def heapify(iStream,j,n): 
   item = iStream[j]
   child = (j * 2)+1
   while child < len(iStream):
        if child+1 < len(iStream) and iStream[child] < iStream[child+1]:
            child = child + 1
        if item >= iStream[child]:
            break
        iStream[child],iStream[(child-1)//2] = iStream[(child-1)//2],iStream[child]
        child = 2*child +1 
   return iStream

def buildheap(iStream,iK):
    n = len(iStream)
    for k in range(n//2-1,-1,-1):
        maxheap=heapify(iStream,k,n) 
    return maxheap

def del_max(maxheap): 
    size=len(maxheap)
    maxheap[0] = maxheap[size-1] 
    maxheap = maxheap[:size-1] 
    return heapify(maxheap,0,size-2)

def ins_max_heap(maxheap,elem): 
    maxheap[0]= elem
    return heapify(maxheap,0,len(maxheap)-1)

lst = [ 12, 24,3, 7,9,18] #N 
p=5 #P
iS = [ x-5 for x in lst ]
print iS
iK = 4 #K
maxheap= buildheap(iS[:iK],iK)

for elem in iS[iK:]:
    if elem < maxheap[0]:
         maxheap = ins_max_heap(maxheap,elem)

print '%d points which are nearest to %d are below in descending order' %(iK,p)
print [x+p for x in maxheap]         

