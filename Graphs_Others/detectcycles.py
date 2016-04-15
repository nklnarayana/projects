#problem: detect a cycle in DAG .
# Cosntruct DFS for each tree, considering each node as root of tree
# To detect a cycle , we can check for cycle in individual trees by checking back edges
# keep track of vertices currently in recursion stack
# if we reach a vertex that is already in recusrion stack , a cycle is detected
class graph(object):
     def __init__(self,n):
           self.vmap={}
           self.num_nodes =n

     def add_edge(self,start,end):
     #_vmap: {vertex x: x's adjacency list}
           if self.vmap.has_key(start):
                 self.vmap[start].append(end)
           else:
                 self.vmap[start] =[end]
     #perform dfs 
     def iscyclic(self,v,visited,recstack):
          if visited[v] == False:
             visited[v] = True
             recstack[v] = True
             # if current vertex has any adjacency vertexes
             if self.vmap.has_key(v):
                 for nextvertex in  self.vmap[v]:
                    # if nextvertex is not visted and if there is a cycle in tree starting with next vertex
                    if not visited[nextvertex]  and self.iscyclic(nextvertex,visited,recstack):
                       return True          
                    # if nextvertex is in recursion stack
                    elif recstack[nextvertex] == True:
                       return True
          # set recstack of vertex v as False so that in the next DFS of another tree, this can be used for detecting cycle, otherwise we get a cycle since it is always marked True after first visit in first DFS of a node.
          recstack[v] = False
          return False

#construct a graph 
def iscyclicmain():
         n=4
         #construct a graph
         g = graph(n)
         g.add_edge(0,1)
         g.add_edge(0,2)
         g.add_edge(1,2)
         #g.add_edge(2,0)
         g.add_edge(2,3)         
         
         print 'adjacency matrix of graph is', g.vmap
         # mark all vertcies as not visted (False)
         visited =[False] * (n) 
         # mark all vertices in recursion stack as False
         recstack =[False] * (n)
         for i in range(0,n):
                if g.iscyclic(i, visited,recstack):
                    return True
         return False 


if iscyclicmain()== True:
    print 'Cycle exists'
else:
    print 'Cycle does not exists'
