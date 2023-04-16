# Hunter Vs Prey v1.3.2

from random import randint, choice
from time import sleep
from os import system
from termcolor import cprint
import sys, tty

def outdated():
    cprint('THIS IS NO LONGER THE NEWEST VERSION!\n', 'green', 'on_red',attrs=['bold'])

T = Tree = "🌳"
P = Prey = "🦊"
H = Hunter = "👨"
M = Mountain = "🍔"

class Animal:
    def __init__(self, speed, direction, moves):
        self.speed = speed
        self.direction = direction
    def end_game():
        system('clear')
        cprint('The hunnter has eaten the prey!','green','on_red')
        cprint(' __     ______  _    _  __          _______ _   _   _ \n \ \   / / __ \| |  | | \ \        / /_   _| \ | | | |\n  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| | | |\n   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` | | |\n    | | | |__| | |__| |    \  /\  /   _| |_| |\  | |_|\n    |_|  \____/ \____/      \/  \/   |_____|_| \_| (_)\n','red')
    def move_right(x,y):
        return x+1,y
    def move_left(x,y):
        return x-1,y
    def move_down(x,y):
        return x,y+1
    def move_up(x,y):
        return x,y-1

class Hunter(Animal):
    def __init__(self, special_move, position_x, position_y):
        self.special_move = special_move
        self.position_x = position_x
        self.position_y = position_y

class Prey(Animal):
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

def show_rule():
    print('Here are the rules:')
    cprint("'W' to move upwards",'red')
    cprint("'A' to move to the left", 'blue')
    cprint("'S' to move downwards",'yellow')
    cprint("'D' to move to the right\n",'magenta')

def begin():
    cprint('Welcome to Hunter Vs Prey!\n', 'green', attrs=['bold'])
    sleep(2)
    cprint('How to win?\nThe goal of this game is to get the hunter to the prey.', 'blue')
    sleep(3)
    system('clear')

def print_map(m):
    result = []
    for row in m:
        vs = [str(v) for v in row]
        result.append(' '.join(vs))
    print("\n".join(result)+'\n')

def reset_map():
    return [[T,T,T,T,T],[T,T,T,T,T],[T,T,T,T,T],[T,T,T,T,T],[T,T,T,T,T]]

def getting_all_free(m):
    free = []
    for y in range(0,5):
        for x in range(0,5):
            if m[y][x] == T:
                free.append([y,x])                
    return free

def neighbours(coordinates,m):
    free_spaces = []
    if m[coordinates[0]-1][coordinates[1]] == T and coordinates[0]-1 != -1:
        free_spaces.append([coordinates[0]-1, coordinates[1]])
    try:
        if m[coordinates[0]+1][coordinates[1]] == T and coordinates[0] != 5:
            free_spaces.append([coordinates[0]+1, coordinates[1]])
    except IndexError:
        pass
    if m[coordinates[0]][coordinates[1]-1] == T and coordinates[1]-1 != -1:
        free_spaces.append([coordinates[0], coordinates[1]-1])
    try:
        if m[coordinates[0]][coordinates[1]+1] == T:
            free_spaces.append([coordinates[0], coordinates[1]+1])
    except IndexError:
        pass
    return free_spaces

def checking(first_free,vaild_spaces, free_spaces, m):
    temp = first_free
    while True:
        for each_thing in vaild_spaces:
            x = neighbours(each_thing,m)
            for each in x:
                if each not in vaild_spaces:
                    vaild_spaces.append(each)
        if temp == vaild_spaces:
            break
        temp = vaild_spaces
    if len(vaild_spaces) == len(free_spaces):
        return True
    return False

def get_mode():
    while True:
        system('clear')
        print('Game mode:')
        cprint('0. Extra Easy', 'blue')
        cprint('1. Easy','green')
        cprint('2. Normal','yellow')
        cprint('3. Hard', 'red')
        cprint('4. Extra Hard', 'magenta')
        print("\nPlease enter game mode:")
        mode = sys.stdin.read(1)
        if mode == '1':
            return 15
        elif mode == '2':
            return 10
        elif mode == '3':
            return 5
        elif mode == '4':
            return 0
        elif mode == '0':
            return 23
        cprint('Invaild input!', 'red')
        sleep(1)

def modify_map():
    mode = get_mode()
    if mode == 0:
        flag = True
    else:
        flag = False
    while True:
        game_map = reset_map()
        used = []
        while len(used) != mode:
            x = randint(0,4)
            y = randint(0,4)
            if [y,x] not in used:   
                used.append([y,x])
        for each in used:
            game_map[each[0]][each[1]]= M
        free_spaces = getting_all_free(game_map)
        vaild_spaces = neighbours(free_spaces[0], game_map)
        if checking(free_spaces[0],vaild_spaces,free_spaces,game_map) == True:
            while True:
                z = randint(0,len(free_spaces)-1)
                x = randint(0,len(free_spaces)-1)
                if z != x:
                    game_map[free_spaces[z][0]][free_spaces[z][1]] = H
                    game_map[free_spaces[x][0]][free_spaces[x][1]] = P
                    break
            return game_map, free_spaces, flag

def get_coordinates(item,animal_type, m):
    for each_line in range(5):
        for each_item in range(5):
            if m[each_line][each_item] == item:
                animal_type.position_x = each_item
                animal_type.position_y = each_line

def get_new_map(new_h_coordinates,new_p_coordinates, m):
    m[Hunter.position_y][Hunter.position_x] = T
    m[new_h_coordinates[1]][new_h_coordinates[0]] = H
    m[Prey.position_y][Prey.position_x] = T
    m[new_p_coordinates[1]][new_p_coordinates[0]] = P

def movement(move,animal_type):
    if move == 'W':
        new_coordinates = Animal.move_up(animal_type.position_x,animal_type.position_y)
    elif move == 'A':
        new_coordinates = Animal.move_left(animal_type.position_x,animal_type.position_y)
    elif move == 'S':
        new_coordinates = Animal.move_down(animal_type.position_x,animal_type.position_y)
    elif move == 'D':
        new_coordinates = Animal.move_right(animal_type.position_x,animal_type.position_y)
    return new_coordinates

def ask_input():
    print('Your move:')
    move = sys.stdin.read(1).upper()
    if move == 'W' or move == 'A' or move =='S' or move =='D':
        new_coordinates = movement(move,Hunter)
        return new_coordinates
    cprint('Wrong input! Try again!', 'red')

def p_move(m, flag):
    number = randint(1,10)
    if number != 3 or flag == True:
        a = 0
        while True:
            temp_x, temp_y = Prey.position_x, Prey.position_y
            if a == 25:
                return [temp_x,temp_y]
            h_place = Hunter.position_x, Hunter.position_y
            random_move = choice('WASD')
            new_coordinates = movement(random_move, Prey)
            if (new_coordinates[0] == -1 or new_coordinates[1] == -1 or new_coordinates[0] > 4 or new_coordinates[1] > 4 or (new_coordinates[0] == h_place[0] and new_coordinates[1] == h_place[1]))or m[new_coordinates[1]][new_coordinates[0]] == M:
                Prey.position_x = temp_x
                Prey.position_y = temp_y
            else:
                break    
            a += 1                  
    return new_coordinates
        
def play():
    tty.setcbreak(0)
    game_map, free_spaces, flag = modify_map()
    system('clear')
    show_rule()
    print_map(game_map)
    while True:
        get_coordinates(H, Hunter, game_map)
        get_coordinates(P, Prey, game_map)
        new_h_coordinates = ask_input()
        if new_h_coordinates != None:
            if new_h_coordinates[0] == -1 or new_h_coordinates[1] == -1 or new_h_coordinates[0] > 4 or new_h_coordinates[1] > 4:
                cprint('Cannot move off the map!', 'red')
                sleep(1)
                system('clear')
            elif game_map[new_h_coordinates[1]][new_h_coordinates[0]] == M:
                cprint('Cannot get up the mountain!', 'red')
                sleep(1)
                system('clear')
            else:
                try: 
                    system('clear')
                    get_new_map(new_h_coordinates,(Prey.position_x, Prey.position_y), game_map)
                    get_coordinates(H, Hunter, game_map)
                    if new_h_coordinates == (Prey.position_x, Prey.position_y):
                        Animal.end_game()
                        break
                    try:
                        p_coordinates = p_move(game_map, flag)
                        get_new_map(new_h_coordinates,p_coordinates,game_map)
                    except UnboundLocalError:
                        pass
                except IndexError:
                    pass
        else:
            sleep(1)
            system('clear')
        show_rule()
        print_map(game_map)
#---------------------------------------------------------------------

begin()
while True:
    play()
    print('\nPlay again? (Y/N)')
    while True:
        again = sys.stdin.read(1).upper()
        if again == 'N'or again == 'Y':
            break
        cprint('Invaild input!', 'red')    
    if again == 'N':
        print('Thank you for playing!')
        break
    system('clear')