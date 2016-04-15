#Problem: duplicated number in a loose permutation of numbers. A permutation is an array that is size N, and also has positive numbers from 1 thru N. A loose permutation is a permutation where some numbers are missing and some are duplicated, but the total number is still N.




def findDuplicateFromPermutation(intArray): 
    print 'given arrays is ', intArray
    for i in range(len(intArray)):
          num = intArray[i] 
          # if the number is already in it's place, move on to next element
          # Else 
          if intArray[i] != i + 1:
                #if values at ith position and (num-1) position are same, then that is the duplicate
                if intArray[num-1] == intArray[i]: 
                     return intArray[i]
                #swap the numbers at ith position and (num-1) th position
                else:
                     temp = intArray[num-1] 
                     intArray[num-1] = intArray[i] 
                     intArray[i] = temp
    return -1


#intArray = [3,4,2,4,5,1]
intArray = [3,4,2,5,1]
print 'duplicate is %d' % findDuplicateFromPermutation(intArray)

