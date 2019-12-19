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
    if x_raw == True and o_raw == True:
        return 0
    elif x_raw:
        return 1
    elif o_raw:
        return 2
    elif ''.join([c for string in field for c in string]).find('_') > 0:
        return 3
    else:
        return 4


answer = ['Impossible', 'X wins', 'O wins', 'Game not finished', 'Draw']
result = 0
cells = input('Enter cells: ')
line = '-' * 9
cells_list = [[c for c in cells[:3]], [c for c in cells[3:6]], [c for c in cells[6:]]]
print(line)
print('|', ' '.join(cells_list[0]), '|')
print('|', ' '.join(cells_list[1]), '|')
print('|', ' '.join(cells_list[2]), '|')
print(line)
if abs(cells.count('X') - cells.count('O')) < 2:
    result = check(cells_list)
print(answer[result])
