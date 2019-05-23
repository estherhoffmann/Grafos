import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from math import inf

A = np.loadtxt('wg59_dist.txt')
G = nx.from_numpy_matrix(A)

#carregar as labels para o grafo
def load_labels(file_):
  labels = {}
  count = 0
  file = open(file_, "r")
  for f in file:
      if '#' not in f:
          labels[count] = f
          count+=1
  return labels

#retorna o vértice com peso mínimo que ainda não foi visitado:
def ExtractMin(Q):
  for i in list(Q):
    if(Q[i] == min(Q.values())):
      return (i)
  else:
    print("ERROR")
    return (None)


def Dijkstra(G):
  #menor custo até o momento para o caminho início->vértice
  MinPathAll = {} 

  #menor custo até o momento para o caminho inicio->vértice, removendo visitados
  MinPathNotVisited = {}  

  #predecessor dos vértices na árvore de caminhos mínimos
  Parent = {}

  #pesos das arestas do grafo G
  Weight = nx.get_edge_attributes(G,'weight')

  #lista de arestas da árvore de caminhos mínimos
  edges = []

  #inicializando valores para todos os vértices
  for i in list(G.nodes()):
    MinPathAll[i] = inf
    Parent[i] = None

  #definindo o(s) vértice(s) inicial(is)
  MinPathAll[0] = 0
  MinPathAll[30] = 0
  MinPathAll[57] = 0
  MinPathNotVisited = MinPathAll

  #quantando há vértices não visitados
  while len(MinPathNotVisited) != 0:

    #atual será o vértice com menor caminho
    current = ExtractMin(MinPathNotVisited)

    #se existir pai para o atual, adicionar a aresta  
    if Parent[current] != None:
      edges.append((Parent[current], current))

    #para cada vizinho do atual
    for adj in list(G.adj[current]):

      #se ele não foi visitado
      if (current, adj) in Weight and adj in MinPathNotVisited:

        #se o caminho min for maior que o caminho do atual+peso da aresta seguinte
        if MinPathAll[adj] > (MinPathAll[current] + Weight[(current, adj)]):
          #atualiza o valor do caminho minimo do vizinho
          MinPathAll[adj] = MinPathAll[current] + Weight[(current, adj)]
          MinPathNotVisited[adj] =  MinPathAll[adj]
          #define o atual como pai do vizinho
          Parent[adj] = current

      #mesma coisa, para (adj, current) no grafo
      elif (adj, current) in Weight and adj in MinPathNotVisited:
        if MinPathAll[adj] > (MinPathAll[current] + Weight[(adj, current)]):
          MinPathAll[adj] = MinPathAll[current] + Weight[(adj, current)]
          MinPathNotVisited[adj] =  MinPathAll[adj]
          Parent[adj] = current

    #removo o atual dos não visitados
    del MinPathNotVisited[current]

  return edges 

#desenha o grafo
def print_min_path_tree(G, edges, labels):
  pos = nx.kamada_kawai_layout(G)
  for (u,v) in edges:
    if (u,v) not in list(G.edges()):
      edges.remove((u, v))
      edges.append((v, u))
  nx.draw(G, pos, edgelist=edges, labels=labels)
  plt.show()


labels = load_labels("wg59_name.txt")


print("\nCaminho mínimo nosso algoritmo: ")
MinPath = Dijkstra(G)
print(MinPath)

print_min_path_tree(G, MinPath, labels)


print("\nCaminho mínimo Dijkstra NetworkX: ")
MinPathNetworkX = nx.single_source_dijkstra_path(G, 0)
print(MinPathNetworkX)

 