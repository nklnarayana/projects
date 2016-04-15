def MergeSort(intArr): 
    merge(intArr)
    return intArr

def merge(intArr): 
    #print 'intArr is' #print intArr
    l = len(intArr) 
    if l> 1:
        lhalf = intArr[:l//2] 
        rhalf = intArr[l//2:]
        
        merge(lhalf)
        merge(rhalf)

        lhalfbegin = 0  #pointer to left half start
        rhalfbegin = 0  #pointer to right half start
        listbegin = 0   # pointer to merged list

        # Rearrange elements of intArr based by comparing elements of lhalf and rhalf    
        while lhalfbegin < len(lhalf) and rhalfbegin < len(rhalf): 
            if lhalf[lhalfbegin] < rhalf[rhalfbegin]:
                intArr[listbegin] = lhalf[lhalfbegin]
                lhalfbegin = lhalfbegin + 1 
            else:
                intArr[listbegin] = rhalf[rhalfbegin]
                rhalfbegin = rhalfbegin + 1
            listbegin = listbegin + 1
     
        # Place remaining elemnts of lhalf into intArr
        while lhalfbegin < len(lhalf): 
            intArr[listbegin] = lhalf[lhalfbegin] 
            lhalfbegin = lhalfbegin + 1 
            listbegin = listbegin +1       

        # Place remaining elements of rhalf into intArr
        while rhalfbegin < len(rhalf):
            intArr[listbegin] = rhalf[rhalfbegin] 
            rhalfbegin = rhalfbegin + 1 
            listbegin = listbegin + 1


intArr = [ 45 , 31, 6, 8 , 11, 9, 98, 76]
print 'Array before sorting', intArr
print 'Array after sorting',  MergeSort(intArr)

