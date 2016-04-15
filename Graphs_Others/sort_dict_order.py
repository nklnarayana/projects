#The idea is to create a graph of characters and then find topological sorting of the created graph. Following are the detailed steps.

#1) Create a graph g with number of vertices equal to the size of alphabet in the given alien language. For example, if the alphabet size is 5, then there can be 5 characters in words. Initially there are no edges in graph.

#2) Do following for every pair of adjacent words in given sorted array.
    #a) Let the current pair of words be word1 and word2. One by one compare characters of both words and find the first mismatching characters.
    #b) Create an edge in g from mismatching character of word1 to that of word2.

#3) Print topological sorting of the above created graph.


class Node:
   def __init__(self):
        self.visited = 'white'
        self.adjacent = []

def printorder(words,alpha):
   graph = {}
   for char in alpha:
       #make each character as a graph node
       graph[char] = Node()
       #{'a': Node(visited,[],'b': Node(visited,[]) }
   for i in xrange(len(words)-1):
       word1 = words[i]
       word2 = words[i+1]
       for j in range(min(len(word1),len(word2))):
           if word1[j] != word2[j]:
                 #if there is a mismatch between characters in word1 and word2
                 # make character in word2 as adjacent to character in word1
                 graph[word1[j]].adjacent.append(word2[j])
            	 break
                 # Very critical. We only compare the first Non-equal char
 
   print topologicalsort(graph)     


#There can be more than one topological sorting for a graph.
#The first vertex in topological sorting is always a vertex with in-degree as 0        
#In DFS, we print a vertex and then recursively call DFS for its adjacent vertices. In topological sorting, we need to print a vertex before its adjacent vertices.




def topologicalsort(graph):
      queue = []                    	
      for node in graph:
          if graph[node].visited == 'white':  
               topologicalsortutil(graph,node,queue)
      return queue


def topologicalsortutil(graph,node,queue):
   if graph[node].visited ==  'gray':
         print 'this is cyclic graph'
   if graph[node].visited == 'white':
      graph[node].visited =  'gray'
      for adja in graph[node].adjacent:
           topologicalsortutil(graph,adja,queue)
      graph[node].visited = 'black'
      queue.insert(0,node)


printorder(['baa','abcd','abca','cab','cad'],'abcd')
printorder(['caa','aaa','aab'],'abc')

               
