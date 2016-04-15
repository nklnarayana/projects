#How many Binary Trees can be constrcuted with n nodes

def  countTrees( iNodeCount):
    if iNodeCount==1 or iNodeCount==0:
         return 1
    else:
         #print 'n is %d' %n
         sums= 0
         left = 0
         right = 0
         for k in range(1,iNodeCount+1):
             left = countTrees(k-1)
             right = countTrees(iNodeCount-k)
             sums = sums + (left * right)
         return sums

#nodes = 4
#nodes = 5
nodes = 10
print 'count of binary trees with %d nodes is %d' %(nodes, countTrees(nodes))
