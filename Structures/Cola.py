class Node():
	def __init__(self,value1):
		self.next = None
		self.value1 = value1

class Queue():
	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0

	def Empty(self):
		return self.size == 0

	def Enqueue(self, value): # Inserta A La Derecha dequeue()
		new_node = Node(value)
		if self.Empty():
			self.first = new_node
			self.last = new_node

		else:
			self.last.next = new_node
			self.last = new_node

		self.size += 1

	def Dequeue(self):
		if self.Empty():
			print("esta vacia")
		else:
			if self.size == 1:
				self.first = self.first.next
				self.last = self.last.next

			else:	
				self.first = self.first.next
			self.size -= 1


	def PrintC(self):
		
		temp = self.first

		while (temp != None):

			print(temp.value1)
	
			temp = temp.next		     	



#PRUEBA
ls = Queue()
ls.Enqueue("1")
ls.Enqueue("2")
ls.Enqueue("3")
ls.PrintC()

print("")

ls.Dequeue()
ls.Dequeue()
ls.Dequeue()

ls.PrintC()

print("\n" + str(ls.size))