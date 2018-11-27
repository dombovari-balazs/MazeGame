# bocsi, de nem futtathato, csak ASCII karakterekkel
import keyboard

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


def movement():
    while True:
        move_up()
        move_down()
        move_left
        move_right


def print_map():
    for line in level_test:
        print(line)


def load_mapFile():
    pass


def move_up():
    if keyboard.is_pressed('w'):
        for 'P' in level_test:
            X = X
            Y = Y + 1


def move_down():
    if keyboard.is_pressed('s'):
        for 'P' in level_test:
            X = X
            Y = Y - 1


def move_left():
    if keyboard.is_pressed('a'):
        for 'P' in level_test:
            X = X - 1
            Y = Y


def move_right():
    if keyboard.is_pressed('d'):
        for 'P' in level_test:
            X = X + 1
            Y = Y


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
