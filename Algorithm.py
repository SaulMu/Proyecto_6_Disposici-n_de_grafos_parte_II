from Graph import Graph
import random as rd
import math as mt
import numpy as np
import random as rd
import copy as cp
from edge import Edges

from PriorityQueue import PriorityQueue



def Malla(n,m, directed = False):
    """
  Genera grafo de malla
  :param m: número de columnas (> 1)
  :param n: número de filas (> 1)
  :param dirigido: el grafo es dirigido?
  :Escribe el grafo
  """
    G = Graph()
    k = 0
    malla = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append(k)
            G.addNode(k)
            k += 1
        malla.append(fila)
    
    for i in range(m):
        for j in range(n):
            if i<m-1:
                G.addEdge(malla[i][j], malla[i+1][j], directed)
            if j<n-1:
                G.addEdge(malla[i][j], malla[i][j+1], directed)

    G.write('Malla', G, n*m)
    return G
    

def ErdosRengy(n,m, directed = False, auto = False):
    """
  Genera grafo aleatorio con el modelo Erdos-Renyi
  :param n: número de nodos (> 0)
  :param m: número de aristas (>= n-1)
  :param dirigido: el grafo es dirigido?
  :param auto: permitir auto-ciclos?
  :Escribe el grafo
  """
    G = Graph()
    for i in range(n):
        G.addNode(i)

    i=0
    while i < m:
        edge = G.addEdge(rd.randint(0,n-1), rd.randint(0,n-1), directed, auto)
        if edge is False:
            i = i
        else:
            i += 1
    G.write('ErgosRengy', G, n)
    return G

def Gilbert(n, p , directed = False, auto = False):
    """
  Genera grafo aleatorio con el modelo Gilbert
  :param n: número de nodos (> 0)
  :param p: probabilidad de crear una arista (0, 1)
  :param dirigido: el grafo es dirigido?
  :param auto: permitir auto-ciclos?
  :Escribe el grafo
  """
    G = Graph()
    for i in range(n):
        G.addNode(i)

    for i in range(n):
        for j in range(n):
            if rd.random() < p:
                if i != j:
                    G.addEdge(i, j)

    G.write('Gilbert', G, n)
    return G

def Geo(n, r ,directed = False, auto = False):

    G = Graph()
    for i in range(n):
        G.addNode(i)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                d = mt.dist(G.nodes.get(i).get('pos'),G.nodes.get(j).get('pos'))
                if d <= r:
                    G.addEdge(i,j, directed, auto)
    G.write('Geo', G, n)
    return G

def Barabási(n, d, directed = False, auto = False ):
    """
  Genera grafo aleatorio con el modelo Barabasi-Albert
  :param n: número de nodos (> 0)
  :param d: grado máximo esperado por cada nodo (> 1)
  :param dirigido: el grafo es dirigido?
  :param auto: permitir auto-ciclos?
  :Escribe el grafo
  """
    G = Graph()
    G.addNode(0)

    for u in range(1, n):
        randomNodes = randomArray(u)
        G.addNode(u)
        for v in range(u):
            deg = G.getDegree(randomNodes[v])
            p = 1 - deg / d
            if rd.random() < p:
                if randomNodes[v] != u:
                    G.addEdge(u, randomNodes[v], directed, auto)
    G.write('Barabasi', G, n)
    return G

def DorogovtsevMendes(n, directed = False):
    """
  Genera grafo aleatorio con el modelo Barabasi-Albert
  :param n: número de nodos (≥ 3)
  :param dirigido: el grafo es dirigido?
  :Escribe el grafo
  """
    G = Graph()
    for i in range(n):
        G.addNode(i)

    G.addEdge(0, 1, directed)
    G.addEdge(1, 2, directed)
    G.addEdge(0, 2, directed)
    for i in range(3, n):
        a = list(np.random.choice(G.edges))
        G.addEdge(a[0], i, directed)
        G.addEdge(a[1], i, directed)
    G.write('Dorogovtsev', G, n)
    return G
    
def randomArray(u):
    '''
    Crea un arreglo aletorio de nodos de 0 a u+1
    param u: numero de nodos
    return arreglo aletorio de nodos
    '''
    newarray = np.random.choice(u, u, replace=False)
    return newarray

def BFS(G, tnodes, mode = None, s = None, write = True):
    '''
    Genera un arbol BFS del grafo G
    :param G: Grafo original
    :param tnodes: numero de nodos del grafo
    :param mode: tipo de grafo generado
    :param s: nodo inicial
    :return BFS: arbol BFS calculado
    '''
    bfs = Graph()
    layers = []
    added = {}
    if write is True:
        print('BFS started ...')
    if s is None:
        seed = rd.choice(list(G.nodes.keys()))
    else:
        seed = s
    n = bfs.addNode(seed)

    layers.append({seed: seed})
    added[seed] = seed
    
    i = 0
    while i < len(layers):
        nextlayer = {}
        curLayer = layers[i]

        for n in curLayer.values():
            edges = G.nodes[n]['edges']
            for e in edges:
                if e[0] == n:
                    m = e[1]
                else:
                    m = e[0]
                if m not in nextlayer and m not in added:
                    nn = bfs.addNode(n)
                    mm = bfs.addNode(m)

                    bfs.addEdge(n, m)
                    nextlayer[m] = m
                    added[m] = m                          
        i += 1
        if len(nextlayer) != 0:
            layers.append(nextlayer)
    if write is True:                                             
        print('BFS finished ...')
    
        bfs.write(f'BFS_{mode}', bfs, tnodes)
    return bfs

def DFS(G, tnodes, mode, s=None):
    '''
    Genera un arbol DFS del grafo G
    :param G: Grafo original
    :param tnodes: numero de nodos del grafo
    :param mode: tipo de grafo generado
    :param s: nodo inicial
    :return DFS: arbol DFS calculado
    '''
    dfs = Graph()
    CopyG = cp.copy(G)
    added = []

    print('DFS started ...')
    if s is None:
        seed = rd.choice(list(CopyG.nodes.keys()))

    else:
        seed = s
    
    nodes = (CopyG.nodes)

    DFS_I(seed, dfs, added, nodes, tnodes, mode)
    DFS_R(seed, dfs, added, nodes, tnodes, mode)

def DFS_I(seed, dfs, added, nodes, tnodes, mode):
    '''
    Genera un arbol DFS mediante el metodo iterativo
    '''
    dfs.addNode(seed)
    added.append(seed)

    CurNode = seed
    while len(dfs.nodes) < tnodes:
        

        if len(nodes[CurNode]['edges']) > 0:
    
            edge = rd.choice(nodes[CurNode]['edges'])
            nextNode = edge[1]

            if nextNode not in added:
                
                dfs.addNode(nextNode)
                dfs.addEdge(CurNode, nextNode)
                added.append(nextNode)

                nodes[CurNode]['edges'].remove(edge)
                invedge = [edge[1], edge[0]]
                nodes[nextNode]['edges'].remove(invedge)

                CurNode = nextNode
            else: 
                nodes[CurNode]['edges'].remove(edge)
                invedge = [edge[1], edge[0]]
                nodes[nextNode]['edges'].remove(invedge)
                CurNode = CurNode
        else:
            for e in dfs.edges:
                if list(e)[1] == CurNode:
                    CurNode = list(e)[0]

    print('DFS_I finished ...')
    dfs.write(f'DFS_I_{mode}', dfs, tnodes)        
    return dfs

def DFS_R(seed, dfs, added, nodes, tnodes, mode):
    '''
    Genera un arbol DFS mediante el metodo recursivo
    '''
    dfs.addNode(seed)
    added.append(seed)


    for e in nodes[seed]['edges']:
        nextNode = e[1]
    
        if nextNode not in added:
            dfs.addNode(nextNode)
            dfs.addEdge(e)
            DFS_R(nextNode, dfs, added, nodes)
    print('DFS_R finished ...')
    dfs.write(f'DFS_R_{mode}', dfs, tnodes)        
    return dfs

def Dijkstra(G, n, mode, s=0):
    '''
    Calcula el camino mas corto de un grafo mediante un algoritmo Dijkstra
    :param G: Grafo original
    :param n: nodos totales del grafo 
    :param mode: tipo de grafo generado
    :param s: nodo inicial
    :return grafo calculado con metodo Dijkstra
    '''
    djt = Graph()

    S = list()
    Pesos = list()
    q = PriorityQueue()
    CopyG = cp.copy(G)
    
    for i in range(n):
        q.insert((float('inf'),i,(0,0)))

    q.update((0,int(s),(0,0)))

   
    while not q.isEmpty():
        peso, u, arista = q.delete()
        S.append(u)
        Pesos.append(peso)
        djt.addNode(u)
        
        if peso != 0:
            djt.addEdge(arista[0], arista[1])
            #CopyG.nodes[arista[0]]['edges'].remove(arista)
            #invedge = [arista[1], arista[0]]
            #CopyG.nodes[arista[1]]['edges'].remove(invedge)
        edges = CopyG.nodes[u]['edges']
        for e in edges:
            v = e[1]
            if v not in S:
                weight = CopyG.getWeight(e)
                if q.value(v) > peso + weight:
            
                    q.update((peso + weight, v, e))
    djt.writeDijkstra(f'Dijkstra_{mode}', djt, n, Pesos)

def KruskalD(G, n, mode):
    '''
    Calcula el arbol de expanción minima de un grafo G mediante un algoritmo Kruksal Directo
    :param G: Grafo original
    :param n: nodos totales del grafo 
    :param mode: tipo de grafo generado
    :return pesototal: peso total de todas las aristas del arbol calculado
    :return arbol calculado con metodo Kruksal Directo
    '''
    q = PriorityQueue()
    
    Edges = G.edges
    m = len(Edges)
    for e in Edges:
        weight = G.getWeight(list(e))
        q.insert((weight,list(e)))

    Group = list()
    for i in range(n):
        Group.append([i])

    krlD = Graph()
    for i  in range(n):
        krlD.addNode(i)

    pesototal = 0
    for i in range(m):
        peso, arista = q.delete()
        u = arista[0]
        v = arista[1]
        group_u = indice(u, Group)
        group_v = indice(v, Group)
     
        if group_u != group_v:
            krlD.addEdge(u, v, False, False, peso)
            Group[group_u].extend(Group[group_v])
            Group.pop(group_v)
            pesototal = pesototal + peso
        
    krlD.write(f'kruskalD_{mode}', krlD, n)
    print(f'Peso total:{pesototal}')
    return pesototal

def KruksalI(G, n, mode):
    '''
    Calcula el arbol de expanción minima de un grafo G mediante un algoritmo Kruksal Inverso
    :param G: Grafo original
    :param n: nodos totales del grafo 
    :param mode: tipo de grafo generado
    :return pesototal: peso total de todas las aristas del arbol calculado
    :return arbol calculado con metodo Kruksal Inverso
    '''
    q = PriorityQueue()
    
    edges = G.edges
    m = len(edges)
    for e in edges:
        weight = G.getWeight(list(e))
        q.insert((weight,list(e)))

    krlI = Graph()
    for i  in range(n):
        krlI.addNode(i)

    pesototal = 0

    for i in range(m):
        peso, arista = q.top()
        CopyG = cp.deepcopy(G)
        CopyG.edges.remove(Edges(arista[0], arista[1], peso))
        CopyG.nodes[arista[0]]['edges'].remove(arista)
        invarista = [arista[1],arista[0]]
        CopyG.nodes[arista[1]]['edges'].remove(invarista)
        
        
        bfs = BFS(CopyG, n, None, None, False)

        if len(bfs.nodes) == n:
            G.edges.remove(Edges(arista[0], arista[1], peso))
            G.nodes[arista[0]]['edges'].remove(arista)
            G.nodes[arista[1]]['edges'].remove(invarista)
        else: 
            krlI.addEdge(arista[0], arista[1], False, False, peso)
            pesototal = pesototal + peso
    
    krlI.write(f'kruskalI_{mode}', krlI, n)
    print(f'Peso total:{pesototal}')
    return pesototal

def Prim(G,n, mode, s=0):
    '''
    Calcula el arbol de expanción minima de un grafo G mediante un algoritmo Prim
    :param G: Grafo original
    :param n: nodos totales del grafo 
    :param mode: tipo de grafo generado
    :param s: nodo inicial
    :return pesototal: peso total de todas las aristas del arbol calculado
    :return arbol calculado con metodo Prim
    '''
    q = PriorityQueue()
    S = list()
    Q = list()
    prm = Graph()
    

    

    for i in range(n):
        Q.append(i)
        prm.addNode(i)

    S.append(s)
    Q.remove(s)
    u = s

    pesototal = 0
    val = 1
    i = 0
    while len(Q) > 0:

        if val == 1:
            val = 0
            edges = G.nodes[u]['edges']
            for e in edges:
                weight = G.getWeight(e)
                q.insert((weight,e))

        peso, arista = q.delete()
        u = arista[0]
        v = arista[1]
        if v not in S:
            S.append(v)
            Q.remove(v)
            prm.addEdge(u, v, False, False, peso)
            u = v
            val = 1
            pesototal += peso
        
        #print(f'iteracion: {i}')
    

    prm.write(f'Prim_{mode}', prm, n)
    print(f'Peso total:{pesototal}')


def indice(node, List):
    '''
    Obtiene el posicion en la que un elemento se encuentra en una matriz
    :param node: nodo que se desea buscar
    :param List: matriz donde buscamos ek nodo
    :return i: indice del nodo
    '''
    for i in range((len(List))):
        if isinstance(List[i],int):
            if node == List[i]:
                return i
        else:
            if node in List[i]:
                return i
            
    



    



    

