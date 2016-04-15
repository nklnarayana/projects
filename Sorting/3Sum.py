#problem :GivenanarrayofNintegers,findalltriplets thatsumtoagiveninteger0(zero).
#* Triplets may or may not be consecutive numbers. * The array can include duplicate elements.
#* Array is not necessarily sorted.


# 1.Sort the input array
# 2.scan the element i in for loop
# 3.have two pointers a) pointer to element next to ith element, b) pointer to element at the end
# 4.negate the ith element to make comparison of start + end element easy  
# 5.a)If sum of start & end equals ith element , increment start by 1 and decrement end by 1
#   b)Else if sum < ith element , increment start by 1
#   c)Else if sum > ith element,  decrement end by 1   
# eleimate duplciate values  there are duplicates 
def printTriplets( intArr): 
    #print intArr
    intArr = sorted(intArr) 
    #print intArr
    ret = []
    for i in range(0,len(intArr)-2):
         if i==0 or intArr[i+1] > intArr[i]: 
             num = -intArr[i]
             start = i + 1
             end = len(intArr)-1
         while start<end:
             if intArr[start] + intArr[end] == num:
                   ret.append([-num ,intArr[start],intArr[end]])
                   start = start + 1
                   end = end -1
                   #increment start by 1  next element is same as current element
                   while start < end and intArr[start] == intArr[start+1]:
                      start = start +1
                   #decrement end by 1  next element is same as current element 
                   while start < end and intArr[end] == intArr[end-1]:
                      end = end - 1
             elif intArr[start] + intArr[end] < num :
                 start = start +1
             elif intArr[start] + intArr[end] > num:
                 end = end -1 
    #print ret
    return ret


if __name__ == '__main__':
    intArr = [ -4,3,0,1,-3,2]
    print printTriplets( intArr)


