import numpy as np
import networkx as nx
from math import inf
from matplotlib import pyplot as plt

#carregar os labels do grafo
def load_labels():
  labels = {}
  count = 0
  file = open("ha30_name.txt", "r")
  for f in file:
      if '#' not in f:
          labels[count] = f.replace("\n", "")
          count+=1
  return labels

#retorna o vértice com peso mínimo que ainda não foi visitado:
def ExtractMin(Q):
  for i in list(Q):
    if(Q[i] == min(Q.values())):
      return (i)
  else:
    print("ERROR")


#algoritmo de prim
def Prim(G, W, initial):

  #dicionário de caminhos mínimos não visitados
  MinEdgeNotVisited = {}

  #dicionário de "pais" dos vértices
  Parent = {}

  #árvore geradora mínima
  MST = []

  #inicializando caminhos mínimos com infinito, e pais como "nenhum"
  for i in list(G.nodes()):
    MinEdgeNotVisited[i] = inf
    Parent[i] = None

  #vértice atual recebe initial (passado por parâmetro)
  current = initial
  
  #como visitamos o vértice atual, remove ele do dicionário de arestas com peso min
  MinEdgeNotVisited.pop(current)


  #para cada um dos vértices restantes:
  for count in range(len(G.nodes()) - 1):


    #para cada vizinho do vértice atual
    for i in list(G.adj[current]):
      if (current, i) in W and i in MinEdgeNotVisited:

        #se o peso entre o atual e o vizinho for menor do que o menor peso já descoberto desse vizinho
        if W[(current, i)] < MinEdgeNotVisited[i]:
          #então o menor peso ja descoberto desse vizinho será alterado para o peso dessa aresta
          MinEdgeNotVisited[i] = W[(current, i)]
          #definimos o vértice atual como pai deste vizinho 
          Parent[i] = current

      #mesma coisa, mas para caso (i, current) esteja no grafo, ao invés de (current, i)
      elif (i, current) in W and i in MinEdgeNotVisited:
        if W[(i, current)] < MinEdgeNotVisited[i]:
          MinEdgeNotVisited[i] = W[(i, current)]
          Parent[i] = current
    
    #vértice atual se torna o vértice que possui o menor peso para ser visitado
    current = ExtractMin(MinEdgeNotVisited)

    #adiciona na MST a aresta (pai do vértice atual, vértice atual)
    MST.append((Parent[current], current))

    #remove o vértice atual do dicionário de arestas de menor peso
    MinEdgeNotVisited.pop(current)
    
  return MST


A = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(A)
W = nx.get_edge_attributes(G,'weight')
labels = load_labels()

#desenha o grafo
pos = nx.kamada_kawai_layout(G)
nx.draw_networkx(G, pos, labels=labels)
plt.show()

MST= Prim(G, W, 0)

#desenha a MST
pos = nx.kamada_kawai_layout(G)
nx.draw_networkx(G, pos, edgelist=MST, labels=labels)
plt.show()

 
