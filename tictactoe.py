def draw(field):
    line = '-' * 9
    print(line)
    print('|', ' '.join(field[0]), '|')
    print('|', ' '.join(field[1]), '|')
    print('|', ' '.join(field[2]), '|')
    print(line)


def check(field):

    def line(char):
        nonlocal field
        test = char * 3
        if (''.join(field[0]) == test or ''.join(field[1]) == test or ''.join(field[2]) == test
            or ''.join([field[i][0] for i in range(3)]) == test or ''.join([field[i][1] for i in range(3)]) == test
            or ''.join([field[i][2] for i in range(3)]) == test or ''.join(field[0][0] + field[1][1] + field[2][2]) == test or ''.join(field[0][2] + field[1][1] + field[2][0]) == test):
            return True
        return False

    x_raw = line('X')
    o_raw = line('O')
    if x_raw and o_raw:
        return 0
    elif x_raw:
        return 1
    elif o_raw:
        return 2
    elif ''.join([c for string in field for c in string]).find(' '):
        return 3
    else:
        return 4

def move(coord):
    global cells_list
    global translate
    c = translate.get(''.join(coord))
    if cells_list[c[0]][c[1]] == ' ':
        cells_list[c[0]][c[1]] = 'X'
        return True
    return False


answer = ['Impossible', 'X wins', 'O wins', 'Game not finished', 'Draw']
result = 0
translate = {'11': [2, 0], '12': [1, 0], '13': [0, 0],
             '21': [2, 1], '22': [1, 1], '23': [0, 1],
             '31': [2, 2], '32': [1, 2], '33': [0, 2]}
# while True:
cells = input('Enter cells: ')
#    if cells == '0':
#        break
cells = cells.replace('_', ' ')
cells_list = [[c for c in cells[:3]], [c for c in cells[3:6]], [c for c in cells[6:]]]
draw(cells_list)
'''
    if abs(cells.count('X') - cells.count('O')) < 2:
        result = check(cells_list)
    print(answer[result])
'''
while True:
    coords = input('Enter the coordinates: ').split()
    if coords[0].isdigit() and coords[1].isdigit():
        if 3 >= int(coords[0]) > 0 and 3 >= int(coords[1]) > 0:
            if move(coords):
                draw(cells_list)
                break
            else:
                print('This cell is occupied! Choose another one!')
        else:
            print('Coordinates should be from 1 to 3!')
    else:
        print('You should enter numbers!')
