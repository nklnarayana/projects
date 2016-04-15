#Given a string s, partition s such that every substring of the partition is a palindrome.
#A single character is considered valid palindrome for this problem.

class Solution:
    def __init__(self):
        self.ret = []
    
    def findpalindrome(self,strInput, plist):
        if len(strInput) ==0 :
            self.ret.append(plist)
        
        for i in range(1,len(strInput)+1):
             if self.isPalindrome(strInput[:i]):
                     self.findpalindrome(strInput[i:], plist + strInput[:i] + '|'   ) 
                     
    def isPalindrome(self,strInput):
        if strInput[:] == strInput[::-1]:
              return True
        else:
              return False
            
def palindromicDecomposition( strInput):
    s= Solution()
    s.findpalindrome(strInput,'')
    return s.ret


#strInput = 'abracadabra'
#strInput = 'desserts'
strInput = 'Neveroddoreven'

lst_strgs =  palindromicDecomposition(strInput)

for lst in lst_strgs:
     print lst



