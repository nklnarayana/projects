#Given an array of numbers, positive integers only, group them in-place into evens and odds.


def groupNumbers( intArr): 

    curr_partition_pos = 0
    for i in range(len(intArr)):
           if intArr[i] % 2 == 0 :
               temp = intArr[i] 
               intArr[i] = intArr[curr_partition_pos] 
               intArr[curr_partition_pos] = temp
               curr_partition_pos = curr_partition_pos + 1
    return intArr


intArr = [ 3,4,-2,7,20,36,8,23,14,11,-1,19,-20]

print groupNumbers(intArr)
