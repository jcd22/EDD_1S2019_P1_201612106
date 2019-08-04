class Node():
	def __init__(self,value1):
		self.next = None
		self.value1 = value1

class Pila():

	def __init__(self):
		self.first = None
		self.size = 0

	def Empty(self):
		return self.size == 0

	def Push(self, value):
		new_node = Node(value)
		if self.Empty():
			self.first = new_node

		else:
			temp = self.first
			self.first = new_node
			self.first.next = temp

		self.size += 1

	def Pop(self):
		if self.Empty():
			print("La Pila Esta Vacia")

		else:
			self.first = self.first.next
			self.size -= 1


	def Imprimir(self):
		
		temp = self.first

		while (temp != None):

			print(temp.value1)
	
			temp = temp.next



#PRUEBA
ls = Pila()
ls.Push("4")
ls.Push("3")
ls.Push("2")
ls.Push("1")

ls.Imprimir()

ls.Pop()
ls.Pop()
ls.Pop()



print("")
ls.Imprimir()
print("\n" + str(ls.size))