#algorithm to find all of the subsets of a set where the number of elements in a set is n

#1. Call findsubsets recursively excluding the last element in list
#2. Start with an empty list (res) to track the subsets in each stage of recursion
#3. Add the subsets   returned by recurson to empty list
#4. Append the last element as a list to  res
#5. for each list in subset of lists returned by recirsion function, add the last element as list and append the concatenate one to res
#6  return res
#7 Base consition: if len(s) == 1 then reurn a list with element in s

def findsubsets(s):
    if len(s) == 1:
        return [s]
    res = []
    subs = findsubsets(s[0:-1]) 
    res = res + subs
    res.append([s[-1]])
    for sub in subs:
        res.append(sub + [s[-1]])
    
    return res
        
s= [1,2,3]        
res = findsubsets(s)
res.append([])
print res
