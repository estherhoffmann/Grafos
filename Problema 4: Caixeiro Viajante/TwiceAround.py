import numpy as np
import networkx as nx
from matplotlib import pyplot as plt


A = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(A)
w = nx.get_edge_attributes(G,'weight')

def load_labels(file_):
  labels = {}
  count = 0
  file = open(file_, "r")
  for f in file:
      if '#' not in f:
          labels[count] = f
          count+=1
  return labels

def TwiceAround(G, initial):

  #encontrando uma árvore mínima do grafo G com ajuda da NetworkX
  mst = nx.minimum_spanning_tree(G)
  
  #tranformando a mst em multigrafo (aceita arestas paralelas)
  mst = nx.MultiGraph(mst)

  #declarando o grafo de resultado do algoritmo
  Graph = nx.Graph()

  #criando uma cópia de mst para usar no 'for' a seguir (não pode ser usada a
  #própria mst pois dentro do 'for' adicionamos elementos em mst)
  mstAux = mst.copy()

  #duplicando as arestas de mst
  for u,v in mstAux.edges():
    mst.add_edge(u,v)

  #encontrando um circuito euleriano em mst com ajuda da NetworkX
  #passando como parâmetro um vérticie inicial 
  euler_circuit = list(nx.eulerian_circuit(mst, initial))
  
  #declaração de uma lista de vértices do circuito de euler, em ordem
  list_nodes_euler = []

  #colocando os valores nesta lista
  for u,v in euler_circuit:
    if u not in list_nodes_euler:
      list_nodes_euler.append(u)
      
    if v not in list_nodes_euler:
      list_nodes_euler.append(v)
      
  #adicionando o vértice inicial ao fim do ciclo
  list_nodes_euler.append(initial)
  
  #populando o grafo de resposta, com o circuito euleriano descoberto
  for node in range(len(G.nodes())):
    parent = list_nodes_euler[node] 
    child = list_nodes_euler[node+1]

    Graph.add_edge(parent,child)
    Graph[parent][child]['weight'] = G[parent][child]['weight'] 
  
  return Graph

Result1 = TwiceAround(G, 0)
Result2 = TwiceAround(G, 1)
Result3 = TwiceAround(G, 2)
Result4 = TwiceAround(G, 3)
Result5 = TwiceAround(G, 4)
Result6 = TwiceAround(G, 5)
Result7 = TwiceAround(G, 6)
Result8 = TwiceAround(G, 7)
Result9 = TwiceAround(G, 8)
Result10 = TwiceAround(G, 9)

labels = load_labels('ha30_name.txt')

nx.draw_networkx(Result1, labels=labels)
plt.show()

#para calcular o peso de cada ciclo gerado
def total_weight(T): 
    weight = 0
    weights = nx.get_edge_attributes(T, 'weight')
    for v in T.edges(): 
        weight += weights[v]
    return weight

custo1 = total_weight(Result1)
custo2 = total_weight(Result2)
custo3 = total_weight(Result3)
custo4 = total_weight(Result4)
custo5 = total_weight(Result5)
custo6 = total_weight(Result6)
custo7 = total_weight(Result7)
custo8 = total_weight(Result8)
custo9 = total_weight(Result9)
custo10 = total_weight(Result10)

print("0: ",custo1,"\n1: ",custo2,"\n2: ",custo3,"\n3: ",custo4,"\n4: ",custo5,"\n5: ",custo6,"\n6: ",custo7,"\n7: ",custo8,"\n8: ",custo9,"\n9: ",custo10)







