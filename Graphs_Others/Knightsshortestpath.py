import sys
# first build the graph for a knight in chess board. A knight can have 8 moves  (2,1), (2,-1),(1,2), (1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2)
# Perform a breadth first search for all  nodes in graoh
# get the shortest path for the end by traversing the prev adjaceny matrix. In below code, i have take end as n*n



class graph(object):
     def __init__(self):
           self.vmap={}
           self.vprev ={}
     def add_edge(self,start,end):
     #_vmap: {vertex x: x's adjacency list}
     #_vprev: {vertex x: x's prev vertex computed by bfs routine}
           if self.vmap.has_key(start):
                 self.vmap[start].append(end)
           else:
                 self.vmap[start] =[end]

     def bfs_shortest(self,start):
         queue =[start]
         self.vprev[start] = None
         
         while len(queue) !=0:
             v = queue[0]
             queue.pop(0)
             if self.vmap.has_key(v):
                  v_adj= self.vmap[v]
             else:
                  continue
             
             for nextv in v_adj:
                  if self.vprev.has_key(nextv):
                         continue
                  else:
                      queue.append(nextv)
                      self.vprev[nextv] = v       

     def get_path(self,end):
          #return shortest path as a list
          v = end
          path = []
          while self.vprev.has_key(v) and self.vprev[v] is not None:
               path.insert(0,v)
               v = self.vprev[v]
          if self.vprev.has_key(v):
               path.insert(0,v)
          else: 
              print 'destination %d does not exist' %v
          return path


class chessboard(object):
     def __init__(self,n):
          self.size =n 
          self.board = graph()
          # a kniight can have 8 valid moves with indices as follows 
          next_point = ( (2,1), (2,-1),(1,2), (1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2) )
          #build graph based on possbile moves for a knight
          for x in range(n):
            for y in range(n):
                start = self.point2index(x, y)
                for dx, dy in next_point:
                    nx = x + dx
                    ny = y + dy

                    if self.is_valid(nx, ny):# check is position is vaild i.e crossing boundaries of chess board
                        end = self.point2index(nx, ny)
                        self.board.add_edge(start, end)    
           
     def is_valid(self,x,y):
         if x >=0 and x < self.size and y >= 0 and y < self.size:
               return True
         else:
               return False

     def point2index(self,x,y):
        #convert a chessboard point to the internal graph vertex 
        return x*self.size + y
   
     def index2point(self,p):
       # convert internal graph vertex  to chessboard point
        return (p / self.size, p % self.size) 


     def solve_knight(self,x,y):
        start = self.point2index(x,y)
        end   = self.point2index(self.size - 1, self.size - 1)
        #perform bfs search for all nodes so that parent of each node can be marked
        self.board.bfs_shortest(start)
        path = [self.index2point(x) for x in self.board.get_path(end)]
        return [(x+1,y+1) for x,y in path]


if __name__ == '__main__':
      N = int(sys.argv[1]) 
      x = int(sys.argv[2])
      y = int(sys.argv[3])
      chess = chessboard(N)
      print chess.solve_knight(x-1,y-1)
       
