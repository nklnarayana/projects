# Problem: You are given a collection of nuts of different size and corresponding bolts. You can choose any nut & any bolt together, from which you can determine whether the nut is larger than bolt, smaller than bolt or matches the bolt exactly. However there is no way to compare two nuts together or two bolts together. (i.e. we cannot sort all nuts or sort all bolts). Write an algorithm to match each bolt to its matching nut.

# The algorithm is to partion by picking last element of bolts as pivot
# rearrange array of nuts and return partition index such that all elements smaller than nuts[i] are on left side and all nuts greater than nuts[i] are on right side
# Next using nuts[i], we can partition the array of bolts
# Now we apply partion recursively on left and right side of nuts

def matchpairs(nuts,bolts,low,high): 
     if low < high :
        pivot = partition(nuts,low,high,bolts[high])
        #use the partition index in nuts as pivot position for partitioning bolts 
        partition(bolts,low,high,nuts[pivot])
        matchpairs ( nuts , bolts , low, pivot - 1 )
        matchpairs(nuts,bolts,pivot+1,high)


#partition lst such that elements to left of pivot are less that it and elements to right of pivot are greater than it
def partition(lst,low,high,pivot): 
    while low<high:
        while lst[low] < pivot: 
           low = low +1
        #print high
        #print lst
        while lst[high] > pivot : 
           high = high - 1
        temp = lst[low] 
        lst[low] = lst[high] 
        lst[high] = temp
    return low

def printmatchedpairs(): 
    print nuts
    print bolts

nuts = [33,12,71,4,154,86,11] 
bolts = [86,4,12,154,33,11,71]

matchpairs(nuts,bolts,0,len(nuts)-1) 

printmatchedpairs()
