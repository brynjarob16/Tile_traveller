# https://github.com/brynjarob16/Tile_traveller

def moveNorth(direction):
    while direction != 'N':
        direction = str(input("Direction: ")).upper()
        if direction == 'N':
            current_tile = 1.2
        else:
            print('Not a valid direction!')
    return direction, current_tile

def moveNorthorEastorSouth(direction):
    while direction != 'N' and direction != 'S' and direction != 'E':
            direction = str(input("Direction: ")).upper()
            if direction == 'N':
                current_tile = 1.3
            elif direction == 'E':
                current_tile = 2.2
            elif direction == 'S':
                current_tile = 1.1
            else:
                print('Not a valid direction!')
        return direction, current_tile

def moveEastorSouth(direction):
    while direction != 'E' and direction != 'S':
            direction = str(input("Direction: ")).upper()
            if direction == 'E':
                current_tile = 2.3
            elif direction == 'S':
                current_tile = 1.2
            else:
                print('Not a valid direction!')
        return direction, current_tile
def moveNorth21(direction):
    while direction != 'N':
            direction = str(input("Direction: ")).upper()
            if direction == 'N':
                current_tile = 2.2
            else:
                print('Not a valid direction!')
        return direction, current_tile

def moveSouthorWest(direction):
    while direction != 'W' and direction != 'S':
            direction = str(input("Direction: ")).upper()
            if direction == 'S':
                current_tile = 2.1
            elif direction == 'W':
                current_tile = 1.2
            else:
                print('Not a valid direction!')
        return direction, current_tile

def moveEastorWest(direction):
    while direction != 'E' and direction != 'W':
            direction = str(input("Direction: ")).upper()
            if direction == 'E':
                current_tile = 3.3
            elif direction == 'W':
                current_tile = 1.3
            else:
                print('Not a valid direction!')
        return direction, current_tile

def moveNorthorSouth(direction):
    while direction != 'N' and direction != 'S':
            direction = str(input("Direction: ")).upper()
            if direction == 'N':
                current_tile = 3.3
            elif direction == 'S':
                current_tile = 3.1
                print('Victory!')
            else:
                print('Not a valid direction!')
        return direction, current_tile

def moveSouthorWest33(direction):
    while direction != 'S' and direction != 'W':
            direction = str(input("Direction: ")).upper()
            if direction == 'S':
                current_tile = 3.2
            elif direction == 'W':
                current_tile = 2.3
            else:
                print('Not a valid direction!')
        return direction, current_tile
   

current_tile = 1.1
s = 'You can travel: '

while current_tile != 3.1:

    if current_tile == 1.1:
       print(s + '(N)orth.')
       direction = ''
       direction, current_tile = moveNorth(direction)

    if current_tile == 1.2:
        print(s + '(N)orth or (E)ast or (S)outh.')
        direction = ''
        direction, current_tile = moveNorthorEastorSouth(direction)

    if current_tile == 1.3:
        print(s + '(E)ast or (S)outh.')
        direction = ''
        direction, current_tile = moveEastorSouth(direction)

    if current_tile == 2.1:
        print(s + '(N)orth.')
        direction = ''
        direction, current_tile = moveNorth21(direction)

    if current_tile == 2.2:
        print(s + '(S)outh or (W)est.')
        direction = ''
        direction, current_tile = moveSouthorWest(direction)
        
    if current_tile == 2.3:
        print(s + '(E)ast or (W)est.')
        direction = ''
        direction, current_tile = moveEastorWest(direction)
    
    if current_tile == 3.2:
        print(s + '(N)orth or (S)outh.')
        direction = ''
        direction, current_tile = moveNorthorSouth(direction)

    if current_tile == 3.3:
        print(s + '(S)outh or (W)est.')
        direction = ''
        direction, current_tile = moveSouthorWest33
       


