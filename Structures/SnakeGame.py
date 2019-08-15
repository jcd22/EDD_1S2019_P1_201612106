'''
    Snake Game Part finished
'''

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint
import ListaDoble##

WIDTH = 35
HEIGHT = 20
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2
SNAKE_LENGTH = 5
SNAKE_X = SNAKE_LENGTH + 1
SNAKE_Y = 3
TIMEOUT = 100

class Snake(object):
    REV_DIR_MAP = {
        KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
        KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT,
    }

    def __init__(self, x, y, window):
        self.snake_list = ListaDoble.DobleList()##
        self.body_list = []
        self.hit_score = 0
        self.timeout = TIMEOUT
        print("adentroSnake")

        for i in range(SNAKE_LENGTH, 0, -1):
            self.body_list.append(Body(x - i, y))
            self.snake_list.insert_node(y, x -i)##

        self.body_list.append(Body(x, y, '0'))
        self.snake_list.insert_node(y, x)##
        self.snake_list.printList()##
        self.window = window
        self.direction = KEY_RIGHT
        self.last_head_coor = (x, y)
        self.direction_map = {
            KEY_UP: self.move_up,
            KEY_DOWN: self.move_down,
            KEY_LEFT: self.move_left,
            KEY_RIGHT: self.move_right
        }

    @property
    def score(self):
        return 'Score : {}'.format(self.hit_score)

    def add_body(self, body_list):
        self.body_list.extend(body_list)

    def eat_food(self, food):
        
        if food.char == '+':

            body = Body(self.last_head_coor[0], self.last_head_coor[1])
            self.snake_list.insert_node(self.snake_list.last.y,self.snake_list.last.x)
            self.body_list.insert(-1, body)#
            self.direction_map[self.direction]()
            self.hit_score += 1
            if self.hit_score % 10 == 0:
                self.timeout -= 9
                self.window.timeout(self.timeout)
        
        else:
            if self.snake_list.size > 3:
                self.hit_score -= 1
                self.snake_list.pop_last()
            else:
                print("limit of the Snake")


        food.reset()

    @property
    def collided(self):
        crack = False
        if self.snake_list.empty() == False:
            temp = self.snake_list.first
            for i in range(self.snake_list.size-1):
                if (self.head.x == temp.x and self.head.y == temp.y):
                    crack = True
                    
                else:
                    temp = temp.next
        return crack


        

    def update(self):
        last_body = self.body_list.pop(0)
        last_part = self.snake_list.pop_last()##
        last_body.x = self.body_list[-1].x
        last_body.y = self.body_list[-1].y
        last_part.x = self.snake_list.last.x ##
        last_part.y = self.snake_list.last.y ##
        self.body_list.insert(-1, last_body)
        self.snake_list.insert_node(last_part.y, last_part.x)
        self.last_head_coor = (self.head.x, self.head.y)
        self.direction_map[self.direction]()
        self.snake_list.printList()

    def change_direction(self, direction):
        if direction != Snake.REV_DIR_MAP[self.direction]:
            self.direction = direction

    def render(self):
        
        if self.snake_list.empty() == False:
            temp = self.snake_list.first
            while temp != None:
                self.window.addstr(temp.y,temp.x,"=")
                temp = temp.next

    @property
    def head(self):
        return self.snake_list.last

    @property
    def coor(self):
        return self.head.x, self.head.y

    def move_up(self):
        
        #self.snake_list.insert_node(self.head.y, self.head.x)
       self.head.y -= 1

       if self.head.y < 1:
            self.head.y = MAX_Y

    def move_down(self):
        self.head.y += 1
        #self.snake_list.insert_node(self.head.y, self.head.x)
        if self.head.y > MAX_Y:
            self.head.y = 1

    def move_left(self):
        self.head.x -= 1
        #self.snake_list.insert_node(self.head.y, self.head.x)
        if self.head.x < 1:
            self.head.x = MAX_X

    def move_right(self):

        self.head.x += 1
        if self.head.x > MAX_X:
            self.head.x = 1

        """if self.head.x > MAX_X:
            self.head.x = 1
            self.snake_list.insert_node(self.head.y, self.head.x)

        else:
            self.head.x += 1
            self.snake_list.insert_node(self.head.y, self.head.x)
"""

class Body(object):
    def __init__(self, x, y, char='='):
        self.x = x
        self.y = y
        self.char = char

    @property
    def coor(self):
        return self.x, self.y

class Food(object):
    def __init__(self, window, char='&'):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
        self.char = char
        self.window = window
        


    def render(self):
        self.window.addstr(self.y, self.x, self.char)

    def reset(self):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
        type1 = randint(0,99)

        if type1 <= 25:
            self.char = '*'# *
        else:
            self.char = '+'# +


class print_snake():



    def main(stdscr):
        stdscr = curses.newwin(HEIGHT, WIDTH, 0, 0)
        stdscr.timeout(TIMEOUT)
        curses.curs_set(0)
        stdscr.border(0)
        stdscr.keypad(1)
        curses.noecho()


        snake = Snake(SNAKE_X, SNAKE_Y, stdscr)
        food = Food(stdscr, '+')

        while True:
            stdscr.clear()
            stdscr.border(0)
            snake.render()
            food.render()

            stdscr.addstr(0, 5, snake.score)
            event = stdscr.getch()

            if event == 27:
                break

            if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
                snake.change_direction(event)

            if snake.head.x == food.x and snake.head.y == food.y:
                snake.eat_food(food)

            if event == 32:
                key = -1
                snake.snake_list.SnakeReport()
                while key != 32:
                    key = stdscr.getch()

            snake.update()
            if snake.collided:
                print("\"collided\"")
                snake.snake_list.SnakeReport()
                break

        #return snake.snake_list


    #curses.wrapper(main)               

        
