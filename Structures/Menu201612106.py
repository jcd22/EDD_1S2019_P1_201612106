import time 
import curses
import ListaDobleEnlaz1

menu = ['Play', 'Scoreboard', 'User Selection', 'Reports', 'Bulk Loading','Exit']
Users = ['Juan', 'Pedro', 'Carlos', 'Fran', 'Walter','Tono']
cir = ListaDobleEnlaz1.DobleList()
bulk = cir.BulkLoad()

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

def main(stdscr):
	
	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
	curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)
	current_row_idx = 0
	SelectedMenu = 
	idMenu  = 1

	print_menu(stdscr,current_row_idx,idMenu)

	while 1:
		key = stdscr.getch()

		stdscr.clear()

		if key == curses.KEY_UP and current_row_idx > 0:
			current_row_idx -= 1
			print_menu(stdscr, current_row_idx,idMenu)
		elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
			current_row_idx += 1
			print_menu(stdscr, current_row_idx,idMenu)
		elif key == curses.KEY_ENTER or key in [10, 13]:
			if current_row_idx == len(menu)-1 and idMenu == 1:
				break

			elif current_row_idx == len(menu)-4 and idMenu == 1:
				stdscr.erase()
				idMenu = 2
				print_menu(stdscr, current_row_idx,2)
			
		stdscr.refresh()
	#time.sleep(3)

curses.wrapper(main)
