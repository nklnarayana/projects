#Input: 10?
#Output: 101,100

#i.e > behaves like a wild card. when ? is replaced by 1 or  0 there are two possibilities for 10?

#Input: 1?0?
#Output: 1000, 1001, 1100,1101

#Write a program that takes given input and produces the suggestd output

# Once the position in wild character is printed with 0 and 1, it should be printed back to wild character so that for the next recursive call, the function should see wild character in that position, othwerwise it would just use what was printed earlier.
def wildchar(input,i):
    if i == len(input) :
        print input
        return
    else:
        if input[i] =='?':
            input[i]=0
            wildchar(input,i+1)
            input[i]=1
            wildchar(input,i+1)
            input[i] = '?'
        else:
            wildchar(input,i+1)
            
        
input = ['1','?','0','?']
wildchar(input,0)

