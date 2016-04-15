#Problem :Given a snake and ladder board, find the minimum number of dice throws required to reach the destination or last cell from source or 1st cell


# Each vertex has 6 adjacency cells (connected) in this game as a throw results numbers 1 to 6 . if there a snake or ladder in those
# 6 numbers, adjacency cell will be top of the ladder cell or tail of snake cell
# idea is to do a bfs of all cells and figure out the shortest path.
# Assume board is built on a list where each entry in list is a cell in board. I assume the board is 6*5 matrix

from collections import deque


#class which stores vertex (cell in chess) and its distance from source
class queueentry:
   def __init__(self,vertex,dist):
       self.vertex =  vertex
       self.dist = dist
   

def getmindicethrows(move,n):
    # The graph has n vertcies. mark all of them as not visited
    visited =[False] * 30
    #create a queue for BFS 
    q = deque()

    #Mark the node 0 as visited
    visited[0] = True
    s = queueentry(0,0)   #distance of 0the vertex is also 0 
    q.append(s) # Enqueue 0th vertex
    while q:
         qe = q[0]
         vertex = qe.vertex
         #if front vertex is the deatination vertex, then we are done
         if vertex == n-1:
             break
         #Otherwise dequeue the front vertex and enqueue 
         #its adjacent vertices( or cell numbers reachable through a dice throw)
         q.popleft()
         for j in range(vertex+1,vertex+7,1):
             if j == n : 
                break
             #if this cell is already visited, then ignore
             if not visited[j]:
                 #otheriwse calculate its distance and mark it as visited
                 
                 dist_of_j = qe.dist + 1
                 visited[j] = True
                 
                 # check if there is a snake or ladder at 'j' 
                 # then tail of snake or top of ladder become adjacent of 'v'
                 if move[j] != -1:
                       adj_vertex = move[j]
                 else:
                       adj_vertex = j
                 adj_qentry = queueentry(adj_vertex,dist_of_j)
                 q.append(adj_qentry)
                 
                     
    return qe.dist     
if __name__ == '__main__':
    n = 30 
    moves = [-1] * 30

    #Ladders 
    moves[2] = 21;
    moves[4] = 7;
    moves[10] = 25;
    moves[19] = 28;
 
    #Snakes
    moves[26] = 0;
    moves[20] = 8;
    moves[16] = 3;
    moves[18] = 6;
    
    print 'min no. of dice throws required is %d' % getmindicethrows(moves,n)
    
