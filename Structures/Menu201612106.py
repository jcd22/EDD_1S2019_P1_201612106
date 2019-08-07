import time 
import curses
import ListaDobleEnlaz1

menu = ['Play', 'Scoreboard', 'User Selection', 'Reports', 'Bulk Loading','Exit']
Users = ['Juan', 'Pedro', 'Carlos', 'Fran', 'Walter','Tono']


def BulkLoading(stdscr):

	cir = ListaDobleEnlaz1.DobleList()
	bulk = cir.BulkLoad()
	return bulk


def print_menu(stdscr, selected_row_idx,idMenu):
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
		bulk = BulkLoading(stdscr)

		for idx, row in enumerate(bulk):
			
			x = w//2 - len(row)//2
			y = h//2 - len(bulk)//2 + idx
			#stdscr.addstr(y, x, row)
			if idx == selected_row_idx:
				stdscr.attron(curses.color_pair(1))
				stdscr.addstr(y, x, row)
				stdscr.attroff(curses.color_pair(1))
			else:
				stdscr.attron(curses.color_pair(2))
				stdscr.addstr(y, x, row)
				stdscr.attroff(curses.color_pair(2))	
	#time.sleep(10)

def movement_menu(stdscr):
	
	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
	curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)
	current_row_idx = 0
	SelectedMenu = None
	idMenu  = 1
	new_bulk = None
	print("adentro")
	print_menu(stdscr,current_row_idx,idMenu)

	while 1:
		key = stdscr.getch()

		stdscr.clear()

		if idMenu == 1:
			SelectedMenu = menu
		elif idMenu == 2:
			bulk = BulkLoading(stdscr)
			SelectedMenu = bulk	

		if key == curses.KEY_UP and current_row_idx > 0:
			current_row_idx -= 1
		elif key == curses.KEY_DOWN and current_row_idx < len(SelectedMenu)-1:
			current_row_idx += 1
		elif key == curses.KEY_ENTER or key in [10, 13]:

			if current_row_idx == len(SelectedMenu)-1 and idMenu == 1: #exit
				break

			elif current_row_idx == len(SelectedMenu)-2 and idMenu == 1: #BulkLoad
				new_bulk = BulkLoading(stdscr)
				stdscr.erase()
				stdscr.addstr(0,0, "The BulkLoad has been completed")
				stdscr.getch()

			elif current_row_idx == len(SelectedMenu)-4 and idMenu == 1:#player select
				stdscr.erase()
				bulk = BulkLoading(stdscr)
				if new_bulk != None:
					idMenu = 2
				else :
					stdscr.addstr(0,0,"Players have not been load")
					stdscr.getch()
				
		print_menu(stdscr,current_row_idx,idMenu)	
		stdscr.refresh()
	#time.sleep(3)

def main(stdscr):

	movement_menu(stdscr)

curses.wrapper(main)
