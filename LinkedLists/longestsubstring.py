#Given a string consisting of opening and closing parenthesis, find length of the longest valid parenthesis substring.

def maxLenMatchingParen( strParenExpression):
    
   
    print strParenExpression
    maxmatchinglength = 0 
    validtill = -1
    
    #Create an empty stack
    stack =[]
    
    #scan each element in string based on index 
    for i in range(0,len(strParenExpression)):
        # if opening parenthesis, push into stack
        if strParenExpression[i] == '(':
            stack.append(i)
        else:
        # if closing parenthesis  
            if len(stack)==0:
                 validtill = -1
            else:
                #pop from stack  if stack is not already empty  
                stack.pop()
                # if stack is empty - there are no opening parenthesis left which were earlier scanned
                # This means start of matching parenthesis will be whole i 
                if len(stack)==0:
                     validtill = -1
                # if stack is not empty, start of matching parenthesis is top of the stack        
                else:
                     validtill = stack[-1]
                # calculate i - validtill which gives max matching lenghth at this end
                # get max of current maxmatchinglength and i - vailidtill 
                maxmatchinglength = max(maxmatchinglength,i-validtill)
    return maxmatchinglength


#strParenExpression = '((())'
#strParenExpression = '()'
#strParenExpression = '()(())'
#strParenExpression = ')))'
#strParenExpression = '(()'
#strParenExpression = '((((())(((()'
print maxLenMatchingParen(strParenExpression)
