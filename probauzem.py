import os
import keyboard
import time
import labirynthMaker

'''
level_test = [
    "XXXXXXXXXX",
    "XP    I  X",
    "XXXX X XXX",
    "X I  X   X",
    "X XX I X X",
    "X X  XXX X",
    "X    I  IX",
    "X IXXX X X",
    "XI     X X",
    "XXXXXXXXFX",
]
'''


def print_map(mapMatrix):
    for line in mapMatrix:
        print(line)


'''
def load_mapFile():
    pass


def buildEmptyMap():
    rows = 10
    columns = 10
    mapMatrix = [[x for x in range(columns)] for x in range(rows)]
    print(mapMatrix)
    return mapMatrix


def buildGameMap(mapKacsa):
    print("We are inside of the buildGameMap()")
    for line in range(10):
        mapKacsa[line] = list(level_test[line])

    for line in mapKacsa:
        print(line)

    return mapKacsa
'''


def movement(map, i, j):
    tema = True
    while tema is True:
        time.sleep(0.08)
        if keyboard.is_pressed('w'):
            if map[i-1][j] == ' ':
                os.system('clear')
                if map[i][j] == 'Þ':
                    map[i][j] = 'O'
                else:
                    map[i][j] = '|'
                map[i-1][j] = 'P'
                i -= 1
                print_map(map)
            elif map[i-1][j] == 'I':
                os.system('clear')
                map[i][j] = '|'
                map[i-1][j] = 'Þ'
                i -= 1
                print_map(map)
            elif map[i-1][j] == 'F':
                os.system('clear')
                tema = False
            elif map[i-1][j] == '-' or '|':
                os.system('clear')
                map = buildEmptyMap()
                map = buildGameMap(map)
                print_map(map)
                i = 1
                j = 1
                continue
            else:
                continue
        if keyboard.is_pressed('s'):
            if map[i+1][j] == ' ':
                os.system('clear')
                if map[i][j] == 'Þ':
                    map[i][j] = 'O'
                else:
                    map[i][j] = '|'
                map[i+1][j] = 'P'
                i += 1
                print_map(map)
            elif map[i+1][j] == 'I':
                os.system('clear')
                map[i][j] = '|'
                map[i+1][j] = 'Þ'
                i += 1
                print_map(map)
            elif map[i+1][j] == 'F':
                os.system('clear')
                tema = False
            elif map[i+1][j] == '-' or '|':
                os.system('clear')
                map = buildEmptyMap()
                map = buildGameMap(map)
                print_map(map)
                i = 1
                j = 1
                continue
            else:
                continue
        if keyboard.is_pressed('a'):
            if map[i][j-1] == ' ':
                os.system('clear')
                if map[i][j] == 'Þ':
                    map[i][j] = 'O'
                else:
                    map[i][j] = '-'
                map[i][j-1] = 'P'
                j -= 1
                print_map(map)
            elif map[i][j-1] == 'I':
                os.system('clear')
                map[i][j] = '-'
                map[i][j-1] = 'Þ'
                j -= 1
                print_map(map)
            elif map[i][j-1] == 'F':
                os.system('clear')
                tema = False
            elif map[i][j-1] == '-' or '|':
                os.system('clear')
                map = buildEmptyMap()
                map = buildGameMap(map)
                print_map(map)
                i = 1
                j = 1
                continue
            else:
                continue
        if keyboard.is_pressed('d'):
            if map[i][j+1] == ' ':
                os.system('clear')
                if map[i][j] == 'Þ':
                    map[i][j] = 'O'
                else:
                    map[i][j] = '-'
                map[i][j+1] = 'P'
                j += 1
                print_map(map)
            elif map[i][j+1] == 'I':
                os.system('clear')
                map[i][j] = '-'
                map[i][j+1] = 'Þ'
                j += 1
                print_map(map)
            elif map[i][j+1] == 'F':
                os.system('clear')
                tema = False
            elif map[i][j+1] == '-' or '|':
                os.system('clear')
                map = buildEmptyMap()
                map = buildGameMap(map)
                print_map(map)
                i = 1
                j = 1
                continue
            else:
                continue
        if keyboard.is_pressed('p'):
            tema = False


def start_timeCounting():
    pass


def message_welcome():
    pass


def message_endGame():
    pass


def catch_flag():
    pass


def change_map():
    pass


def check_movement():
    pass


def movement_toWall():
    pass


def movement_toFlag():
    pass


def movement_toEmpty():
    pass


def displaying(sec):
    start = time.time()
    time.clock()
    elapsed = 0
    while elapsed < sec:
        elapsed = time.time() - start
        time.sleep(1)
    timing = False


def main():
    playing = True
    while playing is True:
        menu = input('Válassz pályát!\n1: Teszt\n2: Open\n3: Trollface\n4: Hexa\n5: Bunny\n6: Quit\n')
        if menu == '1':
            in_maze = True
            while in_maze is True:
                mapCica = labirynthMaker.openTest
                labirynthMaker.print_map2(mapCica, 10)
                movement(mapCica['map'], 1, 1)
                in_maze = False
            timing = True
            while timing is True:
                mapFinal = labirynthMaker.open_screenFinal
                print_map(mapFinal)
                displaying(10)
            continue
        elif menu == '2':
            in_maze = True
            while in_maze is True:
                mapCica = labirynthMaker.open1
                print_map(mapCica)
                movement(mapCica['map'], 1, 1)
                in_maze = False
            timing = True
            while timing is True:
                mapFinal = labirynthMaker.open_screenFinal
                print_map(mapFinal)
                displaying(10)
            continue
        elif menu == '3':
            in_maze = True
            while in_maze is True:
                mapCica = labirynthMaker.openTroll
                print_map(mapCica)
                movement(mapCica['map'], 1, 1)
                in_maze = False
            timing = True
            while timing is True:
                mapFinal = labirynthMaker.open_screenFinal
                print_map(mapFinal)
                displaying(10)
            continue
        elif menu == '4':
            in_maze = True
            while in_maze is True:
                mapCica = labirynthMaker.open_hexa
                print_map(mapCica)
                movement(mapCica['map'], 1, 1)
                in_maze = False
            timing = True
            while timing is True:
                mapFinal = labirynthMaker.open_screenFinal
                print_map(mapFinal)
                displaying(10)
            continue
        elif menu == '5':
            in_maze = True
            while in_maze is True:
                mapCica = labirynthMaker.open_bunny
                print_map(mapCica)
                movement(mapCica['map'], 1, 1)
                in_maze = False
            timing = True
            while timing is True:
                mapFinal = labirynthMaker.open_screenFinal
                print_map(mapFinal)
                displaying(10)
            continue
        elif menu == '6':
            playing = False


main()
