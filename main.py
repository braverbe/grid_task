# Функция для проверки условий головоломки
import math
from itertools import product

def is_valid_solution(solution, grid):
    size = len(grid)
    length = int(math.sqrt(size))

    for i in range(len(solution)):
        # Проверяем условие замкнутости (у каждой клетки ровно 2 соседа)
        try:
            if solution[i] == 1:
                if (solution[i - 1] not in [2, 4, 6]):
                    return False
                if (solution[i + length] not in [3, 4, 5]):
                    return False
            elif solution[i] == 2:
                if (solution[i + 1] not in [1, 3, 6]):
                    return False
                if (solution[i + length] not in [3, 4, 5]):
                    return False
            elif solution[i] == 3:
                if (solution[i - 1] not in [2, 4, 6]):
                    return False
                if (solution[i - length] not in [1, 2, 5]):
                    return False
            elif solution[i] == 4:
                if (solution[i + 1] not in [1, 3, 6]):
                    return False
                if (solution[i - length] not in [1, 2, 5]):
                    return False
            elif solution[i] == 5:
                if (solution[i + length] not in [3, 4]):
                    return False
                if (solution[i - length] not in [1, 2]):
                    return False
            elif solution[i] == 6:
                if (solution[i + 1] not in [1, 3]):
                    return False
                if (solution[i - 1] not in [2, 4]):
                    return False
        except IndexError:
            return False

        #Проверяем на соответствие границам
        if i < length: # Если в первой строке
            if (solution[i] in [3, 4, 5]):
                return False
        if i>=size-length: # Если в последней строке
            if (solution[i] in [1, 2, 5]):
                return False
        if (i%length==0):#Если в левом ряду
            if (solution[i] in [1, 3, 6]):
                return False
        if (i%length==length-1):# Если в правом ряду
            if (solution[i] in [2, 4, 6]):
                return False


        #Проверяем на соответствие таблице точек

        if (grid[i] == 'a'):
            if solution[i] not in [1, 2, 3, 4]:
                return False
        if (grid[i] == 'b'):
            if solution[i] not in [5, 6]:
                return False
    return True


# Функция для генерации всех возможных решений
def generate_solutions(grid):
    size = len(grid)
    solutions = []
    possible_values = range(1, 8)  # Возможные значения от 1 до 7

    # Генерируем все возможные комбинации для клеток
    for solution in product(possible_values, repeat=size):
        # Проверяем, соответствует ли решение условиям головоломки
        if is_valid_solution(solution, grid):
            solutions.append(solution)

    return solutions




# Функция для вывода решений
def print_solutions(solutions, size):
    for solution in solutions:
        print_table(solution, size)
        print('------------')

def print_table(solution, size):
    length = int(math.sqrt(size))
    # Маппинг цифр на соответствующие символы
    symbol_map = {
        1: '\u2510',
        2: '\u250C',
        3: '\u2518',
        4: '\u2514',
        5: '\u2502',
        6: '\u2500',
        7: ' '
    }
    for i in range(length):
        row = solution[i*length: (i+1)*length]
        row_str = ""
        for cell in row:
            row_str += symbol_map[cell] + " "
        print(row_str)
        if i < length - 1:
            print("    ")



if __name__ == "__main__":
    grid = [
        'a', 'b', 'b', 'a',
        'b', '0', '0', 'b',
        'b', '0', '0', 'b',
        'a', 'b', 'b', 'a',
    ]

    # grid = [
    #     'a', 'a',
    #     'a', 'a'
    # ]


    size = len(grid)
    # Генерируем все возможные решения
    solutions = generate_solutions(grid)
    # Выводим решения
    print("Всего решений:", len(solutions))
    print_solutions(solutions, size)





    # print('1', '\u2510')
    # print('2', '\u250C')
    # print('3', '\u2518')
    # print('4', '\u2514')
    # print('5', '\u2502')
    # print('6', '\u2500')
    # print('7', ' ')