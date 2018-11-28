import numpy as np
import networkx as nx
from math import inf

#load names of cities to "labels"
def load_labels():
  labels = {}
  count = 0
  file = open("ha30_name.txt", "r")
  for f in file:
      if '#' not in f:
          labels[count] = f.replace("\n", "")
          count+=1
  return labels

#return next vertex in list of priorities
#(vertex with minimum distance between it and an adjacent visited vertex)
def ExtractMin(Q):
  for i in list(Q):
    if(Q[i] == min(Q.values())):
      return (i)
  else:
    print("ERROR")
    return (None)

#return dictionary with MST's edges as values -> vertex as numbers (if option = 1)
#return list of MST's edges -> vertex as the names of cities (if option != 1)
def Prim(G, labels, option):

  MinPathNotVisited = {}
  Parent = {}
  MST = {}
  MSTcities = []
  
  for i in range(len(G.nodes())):
    MinPathNotVisited[i] = inf
    Parent[i] = None

  Parent[0] = -1
  current = 0

  MinPathNotVisited.pop(0)

  for count in range(len(G.nodes()) - 1):

    for i in list(G.adj[current]):
      if (current, i) in W and i in MinPathNotVisited:
        if W[(current, i)] < MinPathNotVisited[i]:
          MinPathNotVisited[i] = W[(current, i)]
          Parent[i] = current

      elif (i, current) in W and i in MinPathNotVisited:
        if W[(i, current)] < MinPathNotVisited[i]:
          MinPathNotVisited[i] = W[(i, current)]
          Parent[i] = current
    
    current = ExtractMin(MinPathNotVisited)
    MST[count] = (Parent[i], current)
    MSTcities.append((labels[Parent[i]], labels[current]))
    MinPathNotVisited.pop(current)

  if option == 1:
    return MST
  else:
    return MSTcities



#read graph
A = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(A)

#get weight of G edges
W= nx.get_edge_attributes(G,'weight')

labels = load_labels()
MST_num = Prim(G, labels, 1)
MST_names = Prim(G, labels, 2)

print(MST_num)
print(MST_names)


 

