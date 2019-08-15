import time
import curses
import ListaDobleEnlaz1
import SnakeGame
import ListaDoble
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint


menu = ['Play', 'Scoreboard', 'User Selection', 'Reports', 'Bulk Loading','Exit']
menu3 = ['SnakeReport', 'ScoreReport', 'ScoreBoardReport', 'UsersReport', 'Exit']
Users = ['Juan', 'Pedro', 'Carlos', 'Fran', 'Walter','Tono']
cir2 = ListaDobleEnlaz1.DobleList()
temp = ListaDobleEnlaz1.NodeDoble("")
juego = None
list_juego = None
size1 = None
bulke = None
WIDTH = 35
HEIGHT = 20
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2
SNAKE_LENGTH = 5
SNAKE_X = SNAKE_LENGTH + 1
SNAKE_Y = 3
TIMEOUT = 100
"""def BulkLoading(stdscr):

	cir = ListaDobleEnlaz1.DobleList()
	bulk = cir.BulkLoad()
	return bulk
#otra instancia"""


def RunGame(self):

	curses.beep()
	window = curses.newwin()


def print_menu(stdscr, selected_row_idx,idMenu,tempo):

	stdscr.clear()
	h, w = stdscr.getmaxyx()

	if idMenu == 1 :

		for idx, row in enumerate(menu):
			text = "d"
			x = w//2 - len(row)//2
			y = h//2 - len(menu)//2 + idx
			#stdscr.addstr(y, x, row)
			if idx == selected_row_idx:
				stdscr.attron(curses.color_pair(1))
				stdscr.addstr(y, x, row)
				stdscr.attroff(curses.color_pair(1))
			else:
				stdscr.attron(curses.color_pair(2))
				stdscr.addstr(y, x, row)
				stdscr.attroff(curses.color_pair(2))

		stdscr.refresh()

	elif idMenu == 2:

		#bulk = BulkLoading(stdscr)#
		size1 = cir2.getSize()
		bulke = list(range(size1))


		for idx, row in enumerate(bulke):

			x = w//2 - row//2
			y = h//2 - len(bulke)//2 + idx
			#stdscr.addstr(y, x, row)
			if idx == selected_row_idx:
				stdscr.attron(curses.color_pair(1))
				stdscr.addstr(y, x, tempo.cont)
				#stdscr.addstr(y, x, row)
				stdscr.attroff(curses.color_pair(1))
			else:
				stdscr.attron(curses.color_pair(2))
				stdscr.addstr(y, x, tempo.cont)
				#stdscr.addstr(y, x, row)
				stdscr.attroff(curses.color_pair(2))
			#tempo = temp.next
	#time.sleep(10)
	elif idMenu == 3:
		
		size3 = 5
		new_list = list(range(size3))

		for idx, row in enumerate(menu3):
			x = w//2 - len(row)//2
			y = h//2 - len(menu3)//2 + idx

			if idx == selected_row_idx:
				stdscr.attron(curses.color_pair(1))
				stdscr.addstr(y, x, row)
				#stdscr.addstr(y, x, row)
				stdscr.attroff(curses.color_pair(1))
			else:
				stdscr.attron(curses.color_pair(2))
				stdscr.addstr(y, x, row)
				#stdscr.addstr(y, x, row)
				stdscr.attroff(curses.color_pair(2))


def movement_menu(stdscr):

	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
	curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)
	current_row_idx = 0
	SelectedMenu = None
	idMenu  = 1
	new_bulk = None
	new_tempo = None
	print("adentro")
	print_menu(stdscr,current_row_idx,idMenu,new_tempo)

	while 1:
		key = stdscr.getch()

		stdscr.clear()

		if idMenu == 1:
			SelectedMenu = menu


		if key == curses.KEY_UP and current_row_idx > 0:
			current_row_idx -= 1
		elif key == curses.KEY_DOWN and current_row_idx < len(SelectedMenu)-1:
			current_row_idx += 1
		elif key == curses.KEY_ENTER or key in [10, 13]:#AL PRECIONAR ENTER

			if current_row_idx == len(SelectedMenu)-1: #exit
				if idMenu == 1:
					break
				elif idMenu == 3:
					idMenu = 1

			elif current_row_idx == len(SelectedMenu)-2 : #BulkLoad
				#new_bulk = BulkLoading(stdscr)
				if idMenu == 1:
					new_bulk = 1
					cir2.BulkLoad()
					stdscr.erase()
					stdscr.addstr(0,0, "The BulkLoad has been completed")
					stdscr.getch()

				elif idMenu == 3:#SnakeReport
					cir2.UsersReport() # reporte UserReport

			elif current_row_idx == len(SelectedMenu)-3 and idMenu == 1: #Reports
				#
				idMenu = 3
				new_tempo = None
				SelectedMenu = menu3


			elif current_row_idx == len(SelectedMenu)-4 and idMenu == 1:#player select
				stdscr.erase()
				#sbulk = BulkLoading(stdscr)#
				if new_bulk != None:
					idMenu = 2
					temp = cir2.last
					new_tempo = temp
					size1 = cir2.getSize()
					bulke = list(range(size1))
					SelectedMenu = bulke
				else :
					stdscr.addstr(0,0,"Players have not been load")
					stdscr.getch()

			elif current_row_idx == len(SelectedMenu)-5:
				if idMenu == 1:#ScoreBoard
					print("Scoreboard")
				elif idMenu == 3:
					print("snakeReportess")
					list_juego.SnakeReport()

			elif current_row_idx == len(SelectedMenu)-6 and idMenu == 1: #Game selected
				#corre la serpiente
				stdscr.erase()
				stdscr.clear()
				juego = Game(stdscr)
				juego1 = juego.mainSnake()
				list_juego = juego.snake.snake_list
				idMenu = 1
				

		print_menu(stdscr,current_row_idx,idMenu,new_tempo)
		stdscr.refresh()

class Game():
	def __init__(self,stdscr):
		self.stdscr = stdscr
		self.stdscr = curses.newwin(HEIGHT, WIDTH, 0, 0)
		self.stdscr.timeout(TIMEOUT)
		curses.curs_set(0)
		self.stdscr.border(0)
		self.stdscr.keypad(1)
		curses.noecho()
		self.snake = SnakeGame.Snake(SNAKE_X, SNAKE_Y, self.stdscr)
		self.food = SnakeGame.Food(self.stdscr, '+')

		
	def mainSnake(self):
		
		while True:
			self.stdscr.clear()
			self.stdscr.border(0)
			self.snake.render()
			self.food.render()

			self.stdscr.addstr(0, 5, self.snake.score)
			self.stdscr.addstr(0, 25,"level1")
			if self.snake.hit_score >= 10:
				self.stdscr.addstr(0, 25,"level2")

			event = self.stdscr.getch()

			if event == 27:
				break

			if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
				self.snake.change_direction(event)

			if self.snake.head.x == self.food.x and self.snake.head.y == self.food.y:
				self.snake.eat_food(self.food)

			if event == 32:
				key = -1
				self.snake.snake_list.SnakeReport()
				while key  != 32:
					key = self.stdscr.getch()

			self.snake.update()
			if self.snake.collided:
				print("colided")
				self.snake.snake_list.SnakeReport()
				break
      


def main(stdscr):

	movement_menu(stdscr)

curses.wrapper(main)
