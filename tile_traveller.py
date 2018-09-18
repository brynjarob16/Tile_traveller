#The player starts in tile (1,1). At the beginning, and after each move selected by the player, the
#program should print the player’s travel options. If there is an open wall in a direction, write that
#direction as a possible travel direction.
#At each iteration, the player enters the first letter of the direction he/she wishes to travel, after
#which the player should “be” in another tile and the options for the new tile are then printed out.
#The player enters:
# n/N for north (up)
# e/E for east (right)
# s/S for south (down)
# w/W for west (left)
#If the player enters an invalid direction, the program prints “Not a valid direction!” and allows the
#player to enter the direction again.
#For example, in tile (1,1) it’s only possible to move north. In tile (1,2), the possible moves are
#north, east and south, and in tile (3,3) the valid moves are south and west.
#Tile (3,1) is the victory location. When the player enters this tile the program should notify
#him/her of their victory and quit running.
#You can travel: (N)orth.
#Direction: s
#Not a valid direction!
#Direction: n
#You can travel: (N)orth or (E)ast or (S)outh.
#Direction: N
#You can travel: (E)ast or (S)outh.
#Direction: w
#Not a valid direction!
#Direction: E
#You can travel: (E)ast or (W)est.
#Direction: e
#You can travel: (S)outh or (W)est.
#Direction: s
#You can travel: (N)orth or (S)outh.
#Direction: S
#Victory!

start = (1.1)
#n = (N)orth
#e = (E)ast
#s = (S)outh
#w = (W)est

i = 'You can travel'

while start != (3,1):

    if start == (1.1):
        print(i + '(N)orth')
        direction = input('Directon: ')
        direction = direction.upper()
        if direction == 'N':
            start = (1.2)
        else:
            print('Not a valid direction!')
            direction = input('Directon: ')

    if start == (1.2):
        print(i + '(S)outh or (E)ast or (N)orth')
        direction = input('Directon: ')
        direction = direction.upper()
        if direction == 'S':
            start = (1.1)
        elif direction == 'E':
             start = (2.2)
        elif direction == 'N':
            start = (1.3)
        else:
            print('Not a valid direction!')
            direction = input('Directon: ')

    if start == (2.2):
        print(i + '(S)outh or West')
        direction = input('Directon: ')
        direction = direction.upper()
        if direction == 'S':
            start = (2.1)
        elif direction == 'W':
            start = (1,2)
        else:
            print('Not a valid direction!')
            direction = input('Directon: ')

    if start == (2.1):
        print(i + '(N)orth')
        direction = input('Directon: ')
        direction = direction.upper()
        if direction == 'N':
            start = (2.2)
        else:
            print('Not a valid direction!')
            direction = input('Directon: ')
    if start == (1.3):
        print(i + '(S)outh or (E)ast')
        direction = input('Directon: ')
        direction = direction.upper()
        if direction == 'S':
            start = (1.2)
        elif direction == 'E':
             start = (2.3)
        else:
            print('Not a valid direction!')
            direction = input('Directon: ')

    if start == (2.3):
        print(i + '(W)est or (E)ast')
        direction = input('Directon: ')
        direction = direction.upper()
        if direction == 'W':
            start = (1.3)
        elif direction == 'E':
             start = (3.3)
        else:
            print('Not a valid direction!')
            direction = input('Directon: ')
    if start == (3.3):
        print(i + '(W)est or South')
        direction = input('Directon: ')
        direction = direction.upper()
        if direction == 'W':
            start = (2.3)
        elif direction == 'S':
             start = (3.2)
        else:
            print('Not a valid direction!')
            direction = input('Directon: ')

    if start == (3.2):
        print(i + '(N)orth or South')
        direction = input('Directon: ')
        direction = direction.upper()
        if direction == 'N':
            start = (3.3)
        elif direction == 'S':
             start = (3.1)
        else:
            print('Not a valid direction!')
            direction = input('Directon: ')

   
       



