import os, sys


class Node():

    def __init__(self, y, x):
        self.next = None
        self.prev = None
        self.y = y
        self.x = x

class DobleList():

    def __init__(self):

        self.first = None
        self.last = None
        self.size = 0

    def empty(self):

        return self.size == 0

    def pop_last(self):
       delated =  self.first
       self.first = self.first.next
       delated.next = None
       self.size -= 1
       print("pop("+str(delated.x)+ "," + str(delated.y) + ")")
       return delated 


    def insert_node(self, y, x):
        newNode = Node(y, x)

        if self.empty():
            self.first = newNode
            self.last = newNode
            self.first.prev = None
            self.last.next = None

        else:
             #temp = self.last
            self.last.next = newNode
            newNode.prev = self.last
            self.last = newNode
            self.last.next = None
        self.size = self.size + 1

    def printList(self):
        print("adentro")
        if self.empty() == False:
            temp = self.first
            i = 1

        while ( temp != None):

            print("("+str(temp.x)+ "," + str(temp.y) + ")")
    
            temp = temp.next
            i += 1

    def SnakeReport(self):

        ContGraf = "digraph G {"+"\n"
        if self.empty():
            print("No Report is empy")

        else:
            i = 1
            temp = self.first
            ContGraf = ContGraf +"final"+"[label=\"NullCabeza\"]"+"\n"
            ContGraf = ContGraf +"0"+"[label=\"Null\"]"+"\n"

            while True:
                ContGraf = ContGraf + str(i)+"[label=\"("+str(temp.x)+","+str(temp.y)+")\"]"+"\n"
                temp = temp.next
                if temp == None:
                    break
                else:
                    i += 1

            ContGraf = ContGraf + str(i)+" -> "+"final;"+"\n"
            while True:
                ContGraf = ContGraf+str(i)+" -> "+str(i-1)+";"+"\n"
                ContGraf = ContGraf+str(i-1)+" -> "+str(i)+";"+"\n"
                if i == 2:
                    ContGraf = ContGraf+str(i-1)+" -> "+"0"+";"+"\n"
                    break
                else:
                    i -= 1

            ContGraf = ContGraf +"\n"+ "}"
            new_file = open('SnakePos.dot','w')
            new_file.write(ContGraf)
            new_file.seek(0)
            comando = " dot -Tpng  SnakePos.dot -o SnakePos.png"
            os.system(comando)
            os.system("SnakePos.png")



"""lista = DobleList()
lista.insert_node(3,4)
lista.insert_node(4,5)
lista.insert_node(5,5)
lista.insert_node(6,5)
lista.printList()
lista.pop_last()
lista.printList()
lista.insert_node(7,5)
lista.printList()
lista.pop_last()
lista.pop_last()
lista.printList()"""

