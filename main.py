from Algorithm import ErdosRengy, Malla, Gilbert, Geo, Barabási, DorogovtsevMendes, BFS, DFS, Dijkstra, KruskalD, KruksalI, Prim
from visualizacion import Ventana

def pedir():
    op = int(input(
        '''◈════Escoja el algoritmo════◈:
        1)Modelo Gm,n de malla
        2)Modelo Gn,m de Erdös y Rényi
        3)Modelo Gn,p de Gilbert
        4)Modelo Gn,r geográfico simple
        5)Variante del modelo Gn,d Barabási-Albert
        6)Modelo Gn Dorogovtsev-Mendes
        ≫'''))
    
    switch(op)

def switch(op):
    'Pide los parametro y manda a llamar a los algoritmos'
    if op == 1:
        while True:
            no = int(input('Numero de columnas: '))
            if no > 1:
                break
        while True:    
            m = int(input('Numero de filas: '))
            if m > 1:
                break
        d = directed()
        Grafo = Malla(no, m, d)
        n = no*m
        mode = 'Malla'
    elif op == 2:
        while True:
            n = int(input('Numero de nodos: '))
            if n>0:
                break
        while True:
            m = int(input('Numero de aristas: '))
            if m >= n - 1:
               break
        d = directed()
        a = auto()
        Grafo = ErdosRengy(n, m, d, a)
        mode = 'ErdosRengy'
    elif op == 3:
        while True:
            n = int(input('Numero de nodos: '))
            if n > 0:
                break
        while True:
            p = float(input('Probabilidad: '))
            if p > 0 and p < 1:
                break
        d = directed()
        a = auto()
        Grafo = Gilbert(n, p, d, a)
        mode = 'Gilbert'
    elif op == 4:
        while True:
            n = int(input('Numero de nodos: '))
            if n > 0:
                break
        while True:
            r = float(input('Distancia: '))
            if r > 0 and r < 1:
                break
        d = directed()
        a = auto()
        Grafo = Geo(n, r, d, a)
        mode = 'Geo'       
    elif op == 5:
        while True:
            n = int(input('Numero de nodos: '))
            if n > 0:
                break
        while True:
            d = float(input('Grado maximo: '))
            if d > 1:
                break
        di = directed()
        a = auto()
        Grafo = Barabási(n, d, di, a)
        mode = 'Barabasi'   
    elif op == 6:
        while True:
            n = int(input('Numero de nodos: '))
            if n >= 3:
                break
        d = directed()
        Grafo = DorogovtsevMendes(n, d)
        mode = 'DorogovtsevMendes'   
    else:
        pedir()
    dfsybfs(Grafo, n, mode)

def directed():
    'Define si el grafo es dirigido'
    d = input('¿Dirigido? Y/N = ')
    if d == 'N':
        return False
    elif d == 'Y':
        return True
    else:
        directed()

def auto():
    'Define si el grafo contiene bucles'
    a = input('¿Bluces? Y/N = ')
    if a == 'N':
        return False
    elif a == 'Y':
        return True
    else:
        auto()

def dfsybfs(Grafo, n, mode):
    op = int(input(
        '''◈════Escoja el algoritmo════◈:
        1)BFS 
        2)DFS iterativo y recursivo
        3)Dikjstra
        4)Kruskal directo e inverso
        5)Prim
        6)Pygame
        7)Salir
        ≫'''))
    switch2(op, Grafo, n, mode)

def switch2(op, Grafo, n, mode):
    'Pide los parametro y manda a llamar a los algoritmos BFS, DFS, Dijkstra, Kruskal'
    if op == 1:
        bfs = BFS(Grafo, n, mode)
        pygame = Ventana(bfs)
        pygame.ejecutar()
        dfsybfs(Grafo, n, mode)
    elif op == 2:
        DFS(Grafo, n, mode)
        dfsybfs(Grafo, n, mode)
    elif op == 3:
        seed = input("Seed: ")
        Dijkstra(Grafo, n, mode, seed) 
    elif op == 4:
        KruskalD(Grafo, n, mode)
        KruksalI(Grafo, n, mode)
        dfsybfs(Grafo, n, mode)
    elif op == 5:
        Prim(Grafo, n, mode)
        dfsybfs(Grafo, n, mode)
    elif op == 6:
        pygame = Ventana(Grafo)
        pygame.ejecutar()
    elif op == 7:
        return
    else:
        dfsybfs(Grafo, n, mode)

 
pedir()