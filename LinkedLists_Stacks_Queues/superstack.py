#Given a stack, empty at the start, and a series if operations on that stack,  you need to take a peek ath value on top of the stack and print it to output
#after every peration. if stack is empty the print "EMPTY"

#Allowable Operations:
#push a  //Push and element with value a to the top of the stack
#pop     //Pop the top element from the stack
#inc x d //Add the value d to each of teh bottom x elements on the stack

#Input Format:
#n - Integer, number of operations, on the top line
#n lines with exactly one operation per line from the list above

#Output format
#n lines of text, with the elemnet at the top[ of the stak on each line
#If stack is empty, then print "EMPTY"

global stack
stack = []

def supstack(text):
  lines = text.split("""\n""")


  #print len(lines)
  for operation in lines:
   if 'push' in operation :
        stack.append(int(operation[5:]))
        print stack[-1]
   elif 'pop' in operation:
        stack.pop()
        if stack:
           print stack[-1]
        else:
           print 'EMPTY'
   elif 'inc' in operation:
        for i in range(0,int(operation[4])):
             stack[i] = stack[i] + int(operation[6])
        print stack[-1]
        
        
global stack
stack = []
text  = ''

while True:
      line= raw_input()
      if line == 'DONE' :
          break
      text = text + line + """\n"""

#print text
supstack(text)

