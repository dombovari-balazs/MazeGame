# bocsi, de nem futtathato, csak ASCII karakterekkel
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

def handling_input():
    movement_input = input()
    if movement_input == w:
        move_up()
        pass
    if movement_input == a:
        move_left()
        pass
    if movement_input == s:
        move_down()
        pass
    if movement_input == d:
        move_right()
        pass
    
def print_map():
    for line in level_test:
        print(line) 
    
def load_mapFile():
    pass

def buildEmptyMap():
    rows = 10
    columns = 10
    mapMatrix= [[x for x in range(columns)] for x in range(rows)]
    print(mapMatrix)
    return mapMatrix

def buildGameMap(mapKacsa):
    print("We are inside of the buildGameMap()")
    for line in range(10):
        mapKacsa[line] = list(level_test[line])
    
    for line in mapKacsa:
        print(line)
    
    return mapKacsa

def move_up():
    check_movement
    pass
def move_down():
    pass
def move_left():
    pass
def move_right():
    pass

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

print_map()
mapCica = buildEmptyMap()
mapCica = buildGameMap(mapCica)
