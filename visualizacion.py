import pygame
import sys

class Ventana:
    def __init__(self, grafo):
        pygame.init()

        # Definir el tamaño de la ventana
        self.ancho, self.alto = 1000, 700
    

        # Crear la ventana
        self.ventana = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Grafo con Pygame")

        # Definir colores
        self.blanco = (255, 255, 255)
        self.negro = (0, 0, 0)
        self.purpura = (128, 0, 255)

        #Definir Grafo
        self.grafo = grafo

    
    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def actualizar(self, t = None):
        # Lógica de actualización aquí
        #self.grafo.Spring(10,40, 0.25, 2)
        self.grafo.Fruchterman_Reingold(self.ancho, self.alto, t)
        pass
        

    def dibujar(self):
        self.ventana.fill(self.blanco)

         # Dibujar nodos
        #Lista de nodos
        lista_nodos = []
        for x in range(len(self.grafo.nodes)):
            lista_nodos.append(x)
        
        #Posicion de nodos
        pos_nodos = [self.grafo.nodes[x]['pos'] for x in lista_nodos]

        #Calculamos la posicion minima y maxima del conjunto de nodos
        max_posx = 0
        min_posx = 100000
        for x in pos_nodos:
            if x[0] > max_posx:
                max_posx = x[0]
            if x[0] < min_posx:
                min_posx = x[0]
       
        max_posy = 0
        min_posy = 100000
        for x in pos_nodos:
            if x[1] > max_posy:
                max_posy = x[1]
            if x[1] < min_posy:
                min_posy = x[1]

        #Se calcula la escala para mostrarlo en pantalla
        escalax = (max_posx - min_posx)/self.alto
        escalay = (max_posy - min_posy)/self.ancho
        escala = 1/max(escalax, escalay)

        #Se actualiza la posición de los nodos escalada
        pos_nodos = [[x[0]*escala, x[1]*escala] for x in pos_nodos]
 
        #--------------------------------------
        #Calculamos la posicion minima y maxima del conjunto de nodos
        max_posx = 0
        min_posx = 100000
        for x in pos_nodos:
            if x[0] > max_posx:
                max_posx = x[0]
            if x[0] < min_posx:
                min_posx = x[0]
       
        max_posy = 0
        min_posy = 100000
        for x in pos_nodos:
            if x[1] > max_posy:
                max_posy = x[1]
            if x[1] < min_posy:
                min_posy = x[1]


        #centro del conjunto de nodos        
        cen_posx = (max_posx + min_posx)/2
        cen_posy = (max_posy + min_posy)/2

        #Centro de la pantalla
        cen_pos = [cen_posx, cen_posy]
        cen_ventana = (self.ancho/2, self.alto/2)

        #Distancia entre ambos centro
        distancia_ventana = [(cen_pos[0] - cen_ventana[0]), (cen_pos[1] - cen_ventana[1])]
        
        #Se actuliza la posición de los nodos
        pos_nodos = [[(x[0] - distancia_ventana[0]), (x[1] - distancia_ventana[1])] for x in pos_nodos]
        
        # Dibujar nodos
        for nodo in pos_nodos:
            pygame.draw.circle(self.ventana, self.purpura, nodo, 5)

        # Dibujar aristas
        aris_nodos =[list(x) for x in self.grafo.edges]
        for arista in aris_nodos:
            pygame.draw.line(self.ventana, self.negro, pos_nodos[arista[0]], pos_nodos[arista[1]], 1)

        # Actualizar la ventana
        pygame.display.flip()

    def ejecutar(self):
        k = 0.1
        
        while True:
            # Establecer la velocidad de actualización
            

            self.manejar_eventos()
            self.dibujar()
            self.actualizar((self.ancho/10)*k)
            k = k/1.001
            pygame.time.Clock().tick(100)
          
         

            


