#code is not working properly. Need to debug

from __future__ import print_function
def queensrecursion(n,array,curr_row):
    print (curr_row)
    print (n)
    if (curr_row == n-1 ):
        for i in range(0,n):
            print ('+-',end="")
        print ("""+\n""")  
        for k in range(0,n):
            for j in range(0,n):
                if array[j] == k :
                    c = '*'
                else:
                    c =''
                print("|%d" % c)
            print("|\n");
            for j in range(0,n):
                print("+-")
            print ("+\n")    
        print("\n")
        return   

    for col in range(0,n):
        # row is index of array
        # col is value in array
        array[curr_row] = col
        prev_row = 0
        for prev_row in range(0,curr_row):
            if array[prev_row] == array[curr_row]:
                break
            if array[prev_row]  - array[curr_row] ==   prev_row - curr_row:
                break
            if array[prev_row]  - array[curr_row] ==   curr_row - prev_row:  
                break
        if prev_row!= curr_row:
                continue
                
        queensrecursion(n,array,curr_row +1)
            

if __name__ == "__main__":
    n = 3
    array = [None] * n
    # pass 0 as row
    queensrecursion(n,array,0)
