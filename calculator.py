var_dict = {}
var_err = ['Invalid assignment', 'Invalid identifier', 'Unknown variable']

operation = {'-': 0, '+': 0, '*': 1, '/': 1, '^': 2, '(': 3, ')': 3}    # Словарь с приоритетом операций


def spliting(data):  # Разбирает строку в список из чисел (как строка) и операторов
    global operation
    if data.count('(') != data.count(')'):      # Проверка оинакового количества скобок
        return 0  # Invalid expression
    if data[0] == '*' or data[-1] == '*':   # Проверка некоректного ввода
        return 0
    if data[0] == '/' or data[-1] == '/':   # Проверка некоректного ввода
        return 0
    if data[0] == '^' or data[-1] == '^':   # Проверка некоректного ввода
        return 0
    dec_l = []  # разобранная строка
    i = 0
    while i < len(data):
        if data[i] in operation:
            if data[i] == '+':
                dec_l.append(data[i])
                i += 1
                while data[i] == '+' and i < len(data):     # В соответствии с заданием убираем повторяющиеся '+'
                    i += 1
                continue
            if data[i] == '-':
                if data[i+1] == '-':
                    i += 1
                    j = 1
                    while data[i] == '-' and i < len(data):     # В соответствии с заданием убираем повторяющиеся '-'
                        i += 1
                        j += 1
                    if j % 2:
                        dec_l.append('-')
                    else:
                        dec_l.append('+')
                    continue
                else:
                    dec_l.append('-')
                    i += 1
                    continue
            if data[i] in list(operation.keys())[2:5]:
                if data[i+1] in list(operation.keys())[2:5]:    # Проверка повторра '*', '/', '^'
                    return 0
                dec_l.append((data[i]))
                i += 1
                continue
            dec_l.append((data[i]))
            i += 1
            continue
        if data[i].isdigit():
            dec_l.append((data[i]))
            i += 1
            if i == len(data):
                continue
            while i < len(data) and data[i].isdigit():  # Собираем число из цифр
                dec_l[len(dec_l) - 1] += data[i]
                i += 1
            continue
        elif data[i].isalpha():
            dec_l.append((data[i]))
            i += 1
            if i == len(data):
                continue
            while i < len(data) and data[i].isalpha():  # Собираем имя переменной из букв
                dec_l[len(dec_l) - 1] += data[i]
                i += 1
            continue
        elif data[i] == ' ':    # Пропускаем пробелы
            i += 1
    if dec_l[0] == '-' and dec_l[1].isdigit():     # Делаем первое число отрицательным (при необходимости)
        dec_l[1] = dec_l[0] + dec_l[1]
        dec_l.pop(0)
    return dec_l


def in_to_postfix(buff):    # Преобразует входящий список из чисел и операторов в постфиксную форму
    phrase = []  # выражение в постфиксном формате
    op_stack = []  # стек операций
    for x in buff:
        if x == '(':
            op_stack.append(x)
            continue
        if x == ')':
            while op_stack != [] and op_stack[-1] != '(':   # Разбираем стек до левой скобки
                phrase.append(op_stack.pop(-1))
            else:
                op_stack.pop(-1)    # Убираем левую скобку из стека
                continue
        if x.isdigit():
            phrase.append(x)   # Числа храним как str
            continue
        if not op_stack:
            op_stack.append(x)
            continue
        if op_stack[-1] == '(':
            op_stack.append(x)
            continue
        while op_stack != [] and operation.get(x) <= operation.get(op_stack[-1]) and op_stack[-1] != '(':
            phrase.append(op_stack.pop(-1))
        else:
           op_stack.append(x)
           continue
    while op_stack:
        phrase.append(op_stack.pop(-1))
    return phrase



def helper(comm):
    if comm == '/exit':
        return 1
    elif comm == '/help':
        print('''Program support for multiplication *, integer division / and parentheses (...). 
They have a higher priority than addition + and subtraction -.
Also supported power operator ^ that has higher priority than * and /. 
Interpret two adjacent minus signs as a plus.''')
        return 0
    else:
        print('Unknown command')
        return 0


def set_var(data):
    global var_dict
    if data.count('=') > 1:
        return 1
    if data.count('=') == 0 and data.isalpha() and data not in var_dict.keys():
        return 3
    data = data.replace(' ', '')
    number = data[data.find('=') + 1:]
    var = data[:data.find('=')]
    if not var.isalpha():
        return 2
    if number.isalpha():
        if number in var_dict.keys():
            var_dict[var] = var_dict.get(number)
            return 0
        else:
            return 3
    if not number.isdigit():
        return 1
    var_dict[var] = number
    return 0


def calc(data):
    global operation
    stack = []
    for i in data:
        if i.isdigit():
            stack.append(int(i))
            continue
        if i in list(operation.keys()):
            y = stack.pop(-1)
            x = stack.pop(-1)
            if i == '+':
                stack.append(x + y)
                continue
            if i == '-':
                stack.append(x - y)
                continue
            if i == '*':
                stack.append(x * y)
                continue
            if i == '/':
                stack.append(x / y)
                continue
            if i == '^':
                stack.append(x ^ y)
                continue
    return stack.pop(-1)


while True:
    choice = input()
    if choice == '':
        continue
    elif choice[0] == '/':
        if helper(choice):
            break
        else:
            continue
    elif choice[0].isalpha() and '+' not in choice and '-' not in choice:
        if choice in var_dict.keys() and '=' not in choice:
            print(var_dict.get(choice))
            continue
        d = set_var(choice)
        if d:
            print(var_err[d - 1])
        continue
    elif choice.isdigit():
        print('Unknown variable')
        continue
    elif '+' not in choice and '-' not in choice and '*' not in choice and '/' not in choice:
        print('Invalid expression')
        continue
    elif choice.isdigit():
        print(choice)
        continue
    else:
        expression = spliting(choice)
        if not expression:
            print('Invalid expression')
        elif len(expression) == 1:
            print(expression[0])
        else:
            if var_dict:
                for i in range(len(expression)):
                    if expression[i].isalpha():
                        if expression[i] in list(var_dict.keys()):
                            expression[i] = var_dict.get(expression[i])
                        else:
                            print('Unknown variable')
                            continue
            print(int(calc(in_to_postfix(expression))))
print('Bye!')
