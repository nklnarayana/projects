#Implement a power function to raise a double to an int power , including negative powers

def power(base, exponent):
    if exponent ==1 :
         return base
    return base * power(base,exponent-1)


base = 2.5
exponent = -4
if exponent >0 :
    print base * power(base,exponent-1)
elif exponent < 0 :
    exponent = -exponent
    print 1/ ( base * power(base,exponent-1))
else:
    print 1
