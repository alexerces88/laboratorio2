#El programa no soporta las 10 fichas, tomaria demaciado tiempo en mostrar la solucion y da la impresion de que colapsaria la memoria de la pc


import random
import time

class Nodo:
    #self se puede acceder a sus funciones que se esta declarando 
    #hace su funcion para declarar que 

    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = None 
       
        self.set_hijo(hijo)
        
    def set_hijo(self, hijo):
        if (hijo is not None):
            self.hijos.append(hijo)
            if self.hijos is not None:
                for h in self.hijos:
                    h.padre = self
                
    def get_hijos(self):
        return self.hijos
    
    def set_padre(self, padre):
        self.padre = padre
        
    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos
    
    def get_datos(self):
        return self.datos
    
    def set_costo(self, costo):
        self.costo = costo
        
    def get_costo(self):
        return self.costo
    
    def equal(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False
    
    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado
    
    def __str__(self):
        return str(self.get_datos())

def comparar (nodo):
    return nodo.get_costo()
    
def bpa(estado_inicio, estado_solucion,tam):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodos_frontera.append(nodo_inicio)
    
    while resuelto == False and len(nodos_frontera) != 0: #len para contar todos los elementos de una lista 
        nodo_actual = nodos_frontera.pop(0) #el pop es que en una lista saca el ultimo elemento y lo elimina 
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:

            for i in range(0, tam-1):
                hijo1_datos = nodo_actual.get_datos().copy() #para que los valores 
                temp = hijo1_datos[i]
                hijo1_datos[i] = hijo1_datos[i+1]
                hijo1_datos[i+1] = temp
                nRandom=random.randrange(0,1)
                hijo1 = Nodo(hijo1_datos)
                hijo1.set_costo(nRandom)
            
                if not hijo1.en_lista(nodos_visitados) and not hijo1.en_lista(nodos_frontera):
                    nodo_actual.set_hijo(hijo1)
                    nodos_frontera.append(hijo1)
            
if __name__ == "__main__":
    estado_inicial = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start= time.time()
    tam= len(solucion)
    nodo_solucion = bpa(estado_inicial, solucion,tam)
    end=time.time()
    print("El tiempo de ejecucion es: " ,end-start, "segundos.")

    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)