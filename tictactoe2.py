def draw(field):
    line = '-' * 9
    print(line)
    print('|', ' '.join(field[0]), '|')
    print('|', ' '.join(field[1]), '|')
    print('|', ' '.join(field[2]), '|')
    print(line)


def check(char):

    global cells_list
    test = char * 3
    if (''.join(cells_list[0]) == test or ''.join(cells_list[1]) == test or ''.join(cells_list[2]) == test
        or ''.join([cells_list[i][0] for i in range(3)]) == test or ''.join([cells_list[i][1] for i in range(3)]) == test
        or ''.join([cells_list[i][2] for i in range(3)]) == test or ''.join(cells_list[0][0] + cells_list[1][1] + cells_list[2][2]) == test or ''.join(cells_list[0][2] + cells_list[1][1] + cells_list[2][0]) == test):
        return True
    return False


def move(coord, kind):
    global cells_list
    global translate
    c = translate.get(''.join(coord))
    if cells_list[c[0]][c[1]] == ' ':
        if kind:
            cells_list[c[0]][c[1]] = 'X'
        else:
            cells_list[c[0]][c[1]] = '0'
        return True
    return False


step = {1: 'X', 0: 'O'}
translate = {'11': [2, 0], '12': [1, 0], '13': [0, 0],
             '21': [2, 1], '22': [1, 1], '23': [0, 1],
             '31': [2, 2], '32': [1, 2], '33': [0, 2]}

cells_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
draw(cells_list)
step_count = 1
while step_count <= 9:
    coords = input('Enter the coordinates: ').split()
    if coords[0].isdigit() and coords[1].isdigit():
        if 3 >= int(coords[0]) > 0 and 3 >= int(coords[1]) > 0:
            if move(coords, step_count % 2):
                draw(cells_list)
                step_count += 1
                if step_count > 5:
                    if check(step.get((step_count - 1) % 2)):
                        print(step.get((step_count - 1) % 2), 'wins')
                        break
            else:
                print('This cell is occupied! Choose another one!')
        else:
            print('Coordinates should be from 1 to 3!')
    else:
        print('You should enter numbers!')
else:
    print('Draw')
