class NodoDoble():

  def __init__(self,valor):
    self.siguiente = None
    self.anterior - None
    selfl.valor - valor


class DobleEnlazada():

	def __init__(self):
		self.primero = None 
		self.ultimo = None
		self.size = 0

	def estaVacia(self):
	    return self.size == 0

	def insertar_final(self,valor):
		nuevo = NodoDoble(valor)
	    if(self.estaVacia()):
            self.primero = nuevo
            self.ultimo = nuevo
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
        else:
           self.ultimo.sigiente = nuevo
           nuevo.anterior = self.ultimoasia
           self.ultimo = nuevo
           self.ultimo.siguiente = self.primero
           self.primero.anterior = self.ultimo    
           self.size = self.size + 1
    
  def BulkLoad(self):

    todo=""
    x = []
    e=0
    with open('usuarios.csv') as csvfile:
      data = csv.reader(csvfile,delimiter='\n')
      for i in data:
        x.append(i[0])
      while e < len(x):
        if e>0:
          self.Insert(NodeUsers(x[e]))
          todo+=x[e]+"\n"
        e+=1
      archivo = open('usuarios.txt','w')
      archivo.write(todo)
      archivo.seek(0)


