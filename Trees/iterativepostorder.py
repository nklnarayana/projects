#1.push root into stack1
#2.while there are nodes in stack1
   #pop the node from stack1 and push it into stack2
   #push the node.left and node.right into stack1
#3.pop element from stack2 which gives post order traversal
    

class btnode:
   def __init__(self,item):
        self.data = item
        self.left = None
        self.right = None

def postorder(root):

   s1 = []
   s2 = []
   
   #append root to stack
   s1.append(root)

   while len(s1) > 0:
       t=s1.pop()
       s2.append(t)
       
       if t.left: 
            s1.append(t.left)
       if t.right:
            s1.append(t.right)

   # pop from stack2 and print it which gives postorder traversal
   while  len(s2)> 0 :
       print s2.pop().data,


if __name__ == "__main__" :
   root1 = btnode(100)
   root1.left = btnode(50)
   root1.right = btnode(300)
   root1.left.left = btnode(20)
   root1.left.right = btnode(70)

   postorder(root1)
