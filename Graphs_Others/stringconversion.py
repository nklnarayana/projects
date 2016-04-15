#Convert string a to b using a dictionary of words
#construct a graph with node(word) such that each word in the edge differ by 1 character.
#then do a breadth first search to find shortest path 
import time
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


     def isvalidedge(self,s1, s2):
        #print s1,s2
        if len(s1) == len(s2):
            #print s1,s2
            count = 0 
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                   count += 1
            return count <= 1
        else:
            return False
     #perform BFS
     def bfs(self,start,end):
        queue = [] 
        queue.append([start])
        while queue:
             path = queue.pop(0)
             time.sleep(1)
             node = path[-1]
             if node == 'hat':
                 time.sleep(2) 
             if path[-1] == end :
                return path
             if self.vmap.has_key(node):
                 for nextvertex in  self.vmap[node]:
                       time.sleep(2)
                       new_path = list(path)
                       new_path.append(nextvertex)
                       queue.append(new_path)  
                      

dict = ['cat','hat','bad','had']

#print isvalidedge(s1,s2)      
n = 4
g = graph(4)

#construct a graph where an edge exists between two words which differe by exactly one letter.
for i in range(len(dict)):
    for j in range(i+1,len(dict)):
         #print dict[i], dict[j]
         if g.isvalidedge(dict[i],dict[j]):
               print 'here'
               g.add_edge(dict[i],dict[j])

	
  
print g.vmap
print g.bfs('cat','had')
    
