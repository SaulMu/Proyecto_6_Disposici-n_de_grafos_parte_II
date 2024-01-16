import numpy as np
import random

class Node:
    '''
    Clase Nodo
    :atrib edges: lista de aristas del nodo
    :atrib pos: posición del nodo
    '''
    def __init__(self):
        self.edges = []
        self.pos = ([random.random(), random.random()])



    