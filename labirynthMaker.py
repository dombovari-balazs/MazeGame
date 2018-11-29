import string

def buildEmptyMap(columns, rows):
    mapMatrix= [[0 for x in range(columns)] for x in range(rows)]
    return mapMatrix


def print_map(mapMatrix):
    print("You've opened: print_map(mapMatrix)")
    print("Funct: print_map()")
    for line in mapMatrix:
        print(line)


def print_map2(mapMatrix, rows):
    print("You've opened: print_map2(mapMatrix, rows)")
    for y in range(rows):
        for x in range(len(mapMatrix[y])):
            print(mapMatrix[y][x], end='')
        #print()






def format_map_excel(mapMatrix, rows):
    print("You've opened: format_map_excel(mapMatrix, rows)")
    for y in range(rows):
        for x in range(len(mapMatrix[y])):
            if mapMatrix[y][x] == '\t':
                #print("I want to del: ", mapMatrix[y][x])
                #del(mapMatrix[y][x])
                #print("x = ", x) # ez nem biztos, hogy jo. Lehet nem mukszik. Del() mukodesetol fugg
                mapMatrix[y][x] = ''
            elif mapMatrix[y][x] == '\n':
                #print("I want to del: ", mapMatrix[y][x])
                #del(mapMatrix[y][x])
                #print("x = ", x)
                #mapMatrix[y][x] = ' '
                pass
            
            else:
                print(mapMatrix[y][x], end='')
        print()
    return mapMatrix



def format_map_every2nd(mapMatrix, rows):
    print("You've opened: format_map_every2nd(mapMatrix, rows)")
    for y in range(rows):
        for x in range(len(mapMatrix[y])):
            #if mapMatrix[y][x] == '\t':
            if x%2 == 0:
                #print("I want to del: ", mapMatrix[y][x])
                #del(mapMatrix[y][x])
                #print("x = ", x) # ez nem biztos, hogy jo. Lehet nem mukszik. Del() mukodesetol fugg
                if mapMatrix[y][x] == '\t':
                    mapMatrix[y][x] = ''
            elif mapMatrix[y][x] == '\n':
                #print("I want to del: ", mapMatrix[y][x])
                #del(mapMatrix[y][x])
                #print("x = ", x)
                mapMatrix[y][x] = ' '
            
            else:
                print(mapMatrix[y][x], end='')
        print()
    return mapMatrix


def format_map_0finder(mapMatrix, rows):
    print("You've opened: format_map_0finder(mapMatrix, rows)")
    for y in range(rows):
        for x in range(len(mapMatrix[y])):
            #print("Sza")
            if mapMatrix[y][x] == '0':
                #print("Szia! Itt miert nincs semmi?")
                mapMatrix[y][x] = ' '
    return mapMatrix


def openTroll():
    with open('cicaTrollFace.txt', 'r' ) as mazeFileTroll:
        columns = 57
        rows = 58
        mapKacsa = buildEmptyMap(columns,rows)
        i = 0
        for line in mazeFileTroll:
            mapKacsa[i] = list(line)
            #print(list(line))
            i += 1
        print_map2(mapKacsa, rows)



def openTest():
    with open('mazeFileLvl_test.txt', 'r' ) as mazeFileLvl_test:
        columns = 10
        rows = 10
        mapKacsa = buildEmptyMap(columns,rows)
        i = 0
        for line in mazeFileLvl_test:
            mapKacsa[i] = list(line)
            #print(list(line))
            i += 1
        #print_map2(mapKacsa, rows)
        format_map_excel(mapKacsa,rows)
        #print_map2(mapKacsa, rows)
        format_map_0finder(mapKacsa,rows)
        #print_map2(mapKacsa, rows)
        

######################################################################


def open1():
    with open('mazeFileLvl_1.txt', 'r' ) as mazeFileLvl_1:
        columns = 11
        rows = 11
        mapKacsa = buildEmptyMap(columns,rows)
        i = 0
        for line in mazeFileLvl_1:
            mapKacsa[i] = list(line)
            #print(list(line))
            i += 1
        #print_map2(mapKacsa,rows)

######################################################################


def open2():
    with open('mazeFileLvl_2.txt', 'r' ) as mazeFileLvl_2:
        mapKacsa = buildEmptyMap()
        i = 0
        for line in mazeFileLvl_2:
            mapKacsa[i] = list(line)
            #print(list(line))
            i += 1

def open3():
    with open('mazeFileLvl_3.txt', 'r' ) as mazeFileLvl_3:
        mapKacsa = buildEmptyMap()
        i = 0
        for line in mazeFileLvl_3:
            mapKacsa[i] = list(line)
            #print(list(line))
            i += 1

#openTroll()
#openTest()
open1()