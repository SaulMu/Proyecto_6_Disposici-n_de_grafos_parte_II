from node import Node
from edge import Edges
import numpy as np
from math import dist
import math


class Graph:

    def __init__(self):
        '''
        Clase Grafo
        :atrib nodes: Diccionario los nodos del grafo
        :atrib edges: Lista de aristas del grafo
        '''
        self.nodes = {}
        self.edges = []

    def addNode(self, name):
        '''
        Agrega el nodo y sus atributos al diccionario
        :param name: nombre del nodo 
        '''
        node = self.nodes.get(name) 

        if node is None:
            self.nodes[name] = vars(Node())

   
    def addEdge(self, source, target, directed = False, auto = False, weight = None):
        '''
        Agrega el nodo a la lista
        :param source: nodo origen
        :param target: nodo destino
        :param directed: dirigido
        :param auto: ciclos
        :param weight: peso
        '''
        if auto is False:
            buc = source == target
        else:
            buc = False
        if weight == None:
            name = Edges(source, target, np.random.randint(1,100))
        else:
            name = Edges(source, target, weight)
        for edge in self.edges:
            if directed is False:
                comp = name != edge
            else:
                comp = False
            if name == edge or buc or comp:
                return False
        self.edges.append((name))
        self.nodes[source]['edges'].append([source, target])
        self.nodes[target]['edges'].append([target, source])

    def write(self, title, graph, nodes):
        '''
        Genera archivo de grafo con formato GraphViz 
        :param title: titulo del archivo
        :param nodes: numero de nodos
        '''
        with open(f"{title}_{nodes}.gv", "w") as f:
            f.write('Graph = {\n')
            #f.write('layout=circo;\n')
            for node in graph.nodes.keys():
                f.write(f'{node} [label="{node}"];\n')
            for edge in graph.edges:
                arista = list(edge)
                f.write(f'{arista[0]} -> {arista[1]} [label="{edge.weight}"];\n')
            f.write('}\n')
    
    def getDegree(self, node):
        '''
        Obtiene el número de aristas conectadas a un nodo 
        param: node: nodo
        :return grado del nodo
        '''
        deg = 0
        if len(self.edges) > 0:
            for nodes in self.edges:
                if list(nodes)[0] == node or list(nodes)[1] == node:
                    deg += 1
        return deg

    def getWeight(self, edge):
        '''
        Obtiene el peso de la arista 
        :param arista
        :return peso de la arista
        '''
        name = Edges(edge[0],edge[1], 0)
        for edges in self.edges:
            if (edges == name) | (edges != name):
                return edges.weight

    def writeDijkstra(self, title, graph, nodes, pesos):
        '''
        Genera archivo de grafo Dijkstra con formato GraphViz 
        :param title: titulo del archivo
        :param nodes: numero de nodos
        :return pesos: pesos calculados de cada nodo
        '''
        with open(f"{title}_{nodes}.gv", "w") as f:
            f.write('Graph = {\n')
            f.write('layout=sfdp\n')
            i=0
            for node in graph.nodes.keys():
                f.write(f'{node} [label="Nodo{node}_{pesos[i]}"];\n')
                i+=1
            for edge in graph.edges:
                arista = list(edge)
                f.write(f'{arista[0]} -> {arista[1]} \n')
            f.write('}\n')

    def Spring(self, c1, c2, c3, c4):
        '''
        Actiliza la posición de los nodos del grafo por el metodo de Spring
        :param c1: constante de la magnitud fuerza de atracción
        :param c2: constante para regular la distancia estable de las aristas
        :param c3: constante de la magnitud fuerza de repulsion 
        :param c4: constante de la magnitud de la fuerza final ejercida

        '''
        listnodes = self.nodes.keys()
        for node1 in listnodes:
            force_atrac = [0,0]
            force_repel = [0,0]
            pos1 = self.nodes[node1]['pos']
            vecinos = []
            
            for x in self.nodes[node1]['edges']:
                vecinos.append(x[1])

            for node2 in listnodes:
                if node1 == node2:
                    pass
                else:
                    pos2 = self.nodes[node2]['pos']
                    distancia = dist(pos2, pos1)
                    d = [(pos2[0] - pos1[0])/distancia, (pos2[1] - pos1[1])/distancia]
                

                    if node2 in vecinos:
                        magnitud_atrac = [d[0]*c1*math.log(distancia/c2), d[1]*c1*math.log(distancia/c2)]
                        force_atrac = [magnitud_atrac[0] + force_atrac[0], magnitud_atrac[1] + force_atrac[1]]
                        magnitud_repel = [(d[0]*-c3)/math.sqrt(distancia), (d[1]*-c3)/math.sqrt(distancia)]
                        force_repel = [magnitud_repel[0] + force_repel[0], magnitud_repel[1] + force_repel[1]]
                    else:
                        magnitud_repel = [(d[0]*-c3)/math.sqrt(distancia), (d[1]*-c3)/math.sqrt(distancia)]
                        force_repel = [magnitud_repel[0] + force_repel[0], magnitud_repel[1] + force_repel[1]]
            force_total = [(force_atrac[0] + force_repel[0])*c4, (force_atrac[1] + force_repel[1])*c4]
            self.nodes[node1]['pos'] = [pos1[0] + force_total[0], pos1[1] + force_total[1]]

    def Fruchterman_Reingold(self, W, L, t):
        area = W * L 
        k = math.sqrt(area/(len(self.nodes)))
        listnodes = self.nodes.keys()
        force_total = list()
        for node1 in listnodes:
            force_atrac = [0,0]
            force_repel = [0,0]
            pos1 = self.nodes[node1]['pos']
            vecinos = []
            
            for x in self.nodes[node1]['edges']:
                vecinos.append(x[1])
            
            for node2 in listnodes:
                if node1 != node2:
                    pos2 = [self.nodes[node2]['pos'][0], self.nodes[node2]['pos'][1]]
                    distancia = dist(pos2, pos1)+1
                    
                    d = [(pos2[0] - pos1[0])/distancia, (pos2[1] - pos1[1])/distancia]

                    magnitud_repel = [d[0]*(math.pow(k, 2)/distancia), d[1]*(math.pow(k, 2)/distancia)]
                    force_repel = [magnitud_repel[0] + force_repel[0], magnitud_repel[1] + force_repel[1]]
                    if node2 in vecinos:
                        magnitud_atrac = [d[0]*math.pow(distancia, 2)/k, d[1]*math.pow(distancia, 2)/k]
                        force_atrac = [magnitud_atrac[0] + force_atrac[0], magnitud_atrac[1] + force_atrac[1]]

            force_total.append([(force_atrac[0] - force_repel[0]), (force_atrac[1] - force_repel[1])])
        for node1 in listnodes:
            pos1 = self.nodes[node1]['pos']
            mag_force_total = math.sqrt(math.pow(force_total[node1][0], 2) + math.pow(force_total[node1][1], 2))
            direc_force_total = (force_total[node1][0]/mag_force_total, force_total[node1][1]/mag_force_total)
            self.nodes[node1]['pos'] = [pos1[0] + direc_force_total[0]*min(mag_force_total, t), pos1[1] + direc_force_total[1]* min(mag_force_total,t)]
            #self.nodes[node1]['pos'] = [min(W/2, max(-W/2, newpos1[0])), min(L/2, max(-L/2, newpos1[1]))]

        

                        

            









    
            

