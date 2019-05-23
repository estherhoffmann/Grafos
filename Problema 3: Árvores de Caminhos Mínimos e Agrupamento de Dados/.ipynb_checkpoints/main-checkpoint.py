import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from math import inf

A = np.loadtxt('wg59_dist.txt')
G = nx.from_numpy_matrix(A)

def load_labels(file_):
  labels = {}
  count = 0
  file = open(file_, "r")
  for f in file:
      if '#' not in f:
          labels[count] = f
          count+=1
  return labels


def ExtractMin(Q):
  for i in list(Q):
    if(Q[i] == min(Q.values())):
      return (i)
  else:
    print("ERROR")
    return (None)


def Dijkstra(G, initial):
  MinPathAll = {}  #menor custo até o momento para o caminho s-v
  MinPathNotVisited = {}  #menor custo até o momento para o caminho s-v, removendo visitados
  parent = {}       #predecessor de v na árvore de caminhos mínimos
  Weight = nx.get_edge_attributes(G,'weight')
  edges = []
  Dijkstra = {}

  for i in list(G.nodes()):
    MinPathAll[i] = inf
    parent[i] = None

  MinPathAll[0] = 0
  MinPathNotVisited = MinPathAll

  while len(MinPathNotVisited) != 0:
    current = ExtractMin(MinPathNotVisited)  
    if parent[current] != None:
      edges.append((parent[current], current))

    for adj in list(G.adj[current]):
      if (current, adj) in Weight and adj in MinPathNotVisited:
        if MinPathAll[adj] > (MinPathAll[current] + Weight[(current, adj)]):
          MinPathAll[adj] = MinPathAll[current] + Weight[(current, adj)]
          MinPathNotVisited[adj] =  MinPathAll[adj]
          parent[adj] = current
      elif (adj, current) in Weight and adj in MinPathNotVisited:
        if MinPathAll[adj] > (MinPathAll[current] + Weight[(adj, current)]):
          MinPathAll[adj] = MinPathAll[current] + Weight[(adj, current)]
          MinPathNotVisited[adj] =  MinPathAll[adj]
          parent[adj] = current

    del MinPathNotVisited[current]

  return edges 

def print_min_path_tree(G, edges, labels):
  pos = nx.kamada_kawai_layout(G)
  for (u,v) in edges:
    if (u,v) not in list(G.edges()):
      edges.remove((u, v))
      edges.append((v, u))
  nx.draw(G, pos, edgelist=edges, label=labels )
  plt.show()


print("ola")
teste = Dijkstra(G, 1)
print(teste)
labels = load_labels("wg59_name.txt")
print_min_path_tree(G, teste, labels)

teste2 = nx.single_source_dijkstra_path(G, 0)
print(teste2)

 