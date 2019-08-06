import csv
import os, sys
import subprocess

class NodeDoble():

	def __init__(self, cont):

		self.next = None
		self.prev = None
		self.cont = cont

class DobleList():

	def __init__(self):

		self.first = None
		self.last = None
		self.size = 0

	def Empty(self):

		return self.size == 0

	def insert_End(self, content):

		newNode = NodeDoble(content)

		if self.Empty():
			self.first = newNode
			self.last = newNode
			self.first.prev = self.last
			self.last.next = self.first
			self.size += 1

		else:
			self.last.next = newNode
			newNode.prev = self.last
			self.last = newNode
			self.last.next = self.first
			self.first.prev = self.last
			self.size += 1



	def PrintC(self):
	
		if self.Empty() == False:
			temp = self.first
			i = 1

		while ( i <= self.size):

			print(temp.cont)
	
			temp = temp.next
			i += 1

	def BulkLoad(self):
		
		todo=""
		x = []
		e = 0
		with open('usuarios.csv') as csvfile:
			data = csv.reader(csvfile,delimiter='\n')
			for i in data:
				x.append(i[0])
			while e < len(x):
				if e>0:
					self.insert_End(x[e])
					todo += x[e] + "\n"
				e += 1
			archivo = open('usuarios.txt','w')
			archivo.write(todo)
			archivo.seek(0)
			return x					

#prueba
ls = DobleList()
ls.insert_End("1")
ls.insert_End("2")
ls.insert_End("3")




