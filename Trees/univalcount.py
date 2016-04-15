# Problem : Count the number of unival subtrees in a binary tree

#define a binary tree node
class  bnode:
    def __init__(self,item):
       self.val = item
       self.left  = None
       self.right = None
#define function to build a binary tree
def buildbtree():
    node = bnode(10)
    node.left  = bnode(10)
    node.right = bnode(5)
    node.right.left = bnode(5)
    node.right.right = bnode(5)
    node.left.right = bnode(5)

    #return node as root of tree
    return node

# traverse the tree from bottom to top 
# return the counts to the top as traversing is done

def count_unival(node):
    if node is None:
        return True
    islu = count_unival(node.left)
    isru = count_unival(node.right)  

    #if both left and right subtrees are unival
    if islu and isru:
        rl =  node.left
        rr =  node.right
        # if both left and right childs are unival
        if not rl and not rr :
            count.val += 1
            return True
        # if both left and right exists and their values match with parent's val
        elif rl and rr and rl.val ==  node.val and rr.val == node.val:
            count.val += 1
            return True
        # if left node exists and left nodes' value equals its' parent's val
        elif rl and rl.val == node.val:
            count.val += 1
            return True
        #if right node exists and right  nodes' value equals its' parent's val
        elif rr and rr.val == node.val:
            count.val += 1
            return True                     
    
    return False



if __name__ == '__main__':
   root = buildbtree() 
   # create a binary node to track the count of nodes 
   # As traversal is done from bottom to top,I am maintaining a pointer to counter instead of integer as the value does not change during recursion
   # If an interger is used, the count of nodes would be lost as I go up the tree
   count = bnode(0)
   # Call the function to determine count of unival trees
   unival_flag = count_unival(root)
   
   print 'No. of unival trees is %d' %count.val
   

