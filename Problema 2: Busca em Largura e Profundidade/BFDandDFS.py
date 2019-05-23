import networkx as nx
import matplotlib.pyplot as plt
from math import inf

#algoritmo para extrair a BFS-tree
def BFS(G, initial):

  #dicionário com a distância dos vértices
  Distance = {}

  #dicionário com o 'pai' dos vértices
  Parent = {}

  #dicionáio com a cor dos vértices
  Color = {}

  #fila (FIFO - first in, first out)
  Queue = []

  #lista de arestas da árvore extraída
  bfs = []
  
  #inicializando os valores
  for i in list(G.nodes()):
    Color[i] = "WHITE"
    Distance[i] = inf
    Parent[i] = None

  #vértice atual = valor inicial passado como parâmetro
  current = initial

  #cor do vértice inicial torna-se cinza (marca-se como visitado)
  Color[current] = "GRAY"

  #distancia do vértice inicial é definida como 0
  Distance[current] = 0

  #adiciona o vértice inicial à lista
  Queue.append(current)

  #enquanto a lista não estiver vazia
  while len(Queue) != 0:

    #vértice atual se torna o primeiro elem. da fila (e este é removido dela)
    current = Queue.pop(0)

    #se o vértice atual for diferente do inicial
    if current != initial:
      #salva em bfs a aresta (pai do atual, atual)
      bfs.append((Parent[current], current))

    #para cada vizinho do vértice atual
    for adj in list(G.adj[current]):
      #se a cor do vértice vizinho for branca (não foi visitado ainda)
      if Color[adj] == "WHITE":
        Distance[adj] = Distance[current] + 1
        Parent[adj] = current
        Color[adj] = "GRAY"
        Queue.append(adj)

    #marca-se o vértice atual como finalizado
    Color[current] = "BLACK"

  return bfs


#algoritmo para extrair a DFS-tree
def DFS(G, u):
  #lista de vértices visitados
  Explored = []

  #pilha (LIFO - Last In, First Out) inicializada com vértice inicial
  Stack = [u]

  #dicionário dos 'pais' dos vértices
  Parent = {}

  #lista de arestas da árvore extraída
  Dfs = []

  #enquanto a pilha não está vazia
  while len(Stack) != 0:

    #vértice atual recebe ultimo elem. da pilha (e este é removido dela)
    current = Stack.pop()

    #se o atual não foi já visitado
    if current not in Explored:

      #marca como visitado
      Explored.append(current)

      #adiciona a aresta (pai de atual, atual) em Dfs
      if current != u:
        Dfs.append((Parent[current], current))

      #Adj recebe lista de vizinhos do vértice atual
      Adj = list(G.adj[current]) 

      #Lista de vizinhos é ordenada decrescentemente
      Adj.sort(reverse=True, key=int)

      #para cada vizinho não explorado, adicionar ele na pilha
      # e definir o vértice atual como pai dele.
      for w in Adj:
        if w not in Explored:
          Stack.append(w)
          Parent[w] = current

  return Dfs


Karate = nx.read_pajek('karate.paj')
Dolphins = nx.read_pajek('dolphins.paj')


#testando com exercício simples de sala:
H = nx.Graph()
H.add_edges_from([(1, 2), (1, 5), (2, 4), (2, 6), (2, 3), (4, 5), (4, 6), (4, 7), 
(5, 6), (6, 8), (7, 8), (3, 8), (3, 7)])
print("\nExercicio Simples: ")
Exercicio = DFS(H, 1)
print(Exercicio)


print("BFS:")
print("\nKarate: ")
BfsTreeKarate = BFS(Karate, '1')
print("Usando nosso algoritmo: ")
print(BfsTreeKarate)


#para verificar se a BFS-tree está correta:
BfsTreeKarate_NetworkX = list(nx.bfs_edges(Karate, '1'))
print("Usando a função da biblioteca: ")
print(BfsTreeKarate_NetworkX)


print("\nDolphins: ")
BfsTreeDolphins = BFS(Dolphins, '1')
print("Usando nosso algoritmo:")
print(BfsTreeDolphins)

#para verificar se a BFS-tree está correta:
BfsTreeDolphins_NetworkX = list(nx.bfs_edges(Dolphins, '1'))
print("Usando a função da biblioteca: ")
print(BfsTreeDolphins_NetworkX)


print("\n\nDFS:")
print("\nKarate: ")
DfsTreeKarate = DFS(Karate, '1')
print("Usando nosso algoritmo: ")
print(DfsTreeKarate)
#para verificar se a BFS-tree está correta:
DfsTreeKarate_NetworkX = list(nx.dfs_edges(Karate, '1'))
print("Usando a função da biblioteca: ")
print(DfsTreeKarate_NetworkX)



print("\nDolphins: ")
DfsTreeDolphins = DFS(Dolphins, '1')
print("Usando nosso algoritmo: ")
print(DfsTreeDolphins)
#para verificar se a BFS-tree está correta:
DfsTreeDolphins_NetworkX = list(nx.dfs_edges(Dolphins, '1'))
print("Usando a função da biblioteca: ")
print(DfsTreeDolphins_NetworkX)


#desenha a BFS-tree do Karate 
pos = nx.kamada_kawai_layout(Karate)
nx.draw_networkx(Karate, pos, edgelist=BfsTreeKarate    )
plt.show()

#desenha a BFS-tree MST do Dolphin 
pos = nx.kamada_kawai_layout(Dolphins)
nx.draw_networkx(Dolphins, pos, edgelist=BfsTreeDolphins)
plt.show()

#desenha a DFS-tree do Karate 
pos = nx.kamada_kawai_layout(Karate)
nx.draw_networkx(Karate, pos, edgelist=BfsTreeKarate)
plt.show()

#desenha a DFS-tree MST do Dolphin 
pos = nx.kamada_kawai_layout(Dolphins)
nx.draw_networkx(Dolphins, pos, edgelist=BfsTreeDolphins)
plt.show()
