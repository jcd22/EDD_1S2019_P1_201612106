class NodoDoble():


	def __init__(self,valor):
		self.siguiente = None
		self.anterior - None
		selfl.valor - valor

class ListaDoble():

	def __init__(self):
		self,primerro = None
		self.size = 0

	def estaVacia():
	    return self.size == 0	

    def insertar_final(self, valor):
    	if self.estaVacia():
    		self.primer = nevo
    	else:	
            temporal = self.primer #apnta al primero de la lista
            while (temporal.siguiente!=None)
                temporal = temporal.siguiente
            #temporal apunta al ultimo elemento
            #es decir que el sigiente de temporal es null
            temporal.siguiente = nuevo
            nuevo.anterior = temporal    
        self.size = self.size + 1   
