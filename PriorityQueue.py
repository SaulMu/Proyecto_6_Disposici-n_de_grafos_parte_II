

class PriorityQueue(object):
    '''
    Clase Cola de Prioridad
    '''
    def __init__(self):
        '''
        Definimos la cola de prioridad como una lista
        '''
        self.queue = []
 
    def __str__(self):
        '''
        Imprime los datos de la lista 
        '''
        return ' '.join([str(i) for i in self.queue])
 
    
    def isEmpty(self):
        '''
        Checa si la lista esta vacia 
        '''
        return len(self.queue) == 0

    def insert(self, data):
        '''
        Inserta un elemeto a la lista
        '''
        self.queue.append(data)
 
    def delete(self):
        '''
        Elimina el valor con la menor prioridad y lo devuelve
        '''
        try:
            min_val = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[min_val][0]:
                    min_val = i
            item = self.queue[min_val]
            del self.queue[min_val]
            return item 
        except IndexError:
            print()
            exit()
    
    def top(self):
        '''
        Elimina el valor con la mayor prioridad y lo devulve
        '''
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] > self.queue[max_val][0]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item 
        except IndexError:
            print()
            exit()

    def update(self, data):
        '''
        Actiliza la prioridad de un elemento de la lista
        '''
        item = data[1]
        for i in range(len(self.queue)):
            if self.queue[i][1] == item:
                self.queue[i] = data
                break
    
    def value(self, item):
        '''
        Devuelve el valor de prioridad de un elemento de la lista 
        '''
        for items in self.queue:
            if items[1] == item:
                return items[0]


