# Implement towers of Hanoi problem

def movetower(h,fromPole,toPole,withPole):
    if h > 1:
        movetower(h-1,fromPole,withPole,toPole)
        print ' moving disk from %s to %s'   %(fromPole,toPole)   
        movetower(h-1,withPole,fromPole,toPole)
                       
movetower(5,'A','B','C')  
