# Функция для проверки условий головоломки
import math


def is_valid_solution(solution, size):
    length = int(math.sqrt(size))
    # Проверяем условие черного круга
    for i in range(len(solution)):
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

    return True


# Функция для генерации всех возможных решений
def generate_solutions(size):
    solutions = []
    # Генерируем все возможные комбинации для клеток 1-7
    for i1 in range(1, 8):
        for i2 in range(1, 8):
            for i3 in range(1, 8):
                for i4 in range(1, 8):
                    for i5 in range(1, 8):
                        for i6 in range(1, 8):
                            for i7 in range(1, 8):
                                for i8 in range(1, 8):
                                    for i9 in range(1, 8):
                                        solution = [i1, i2, i3,
                                                    i4, i5, i6,
                                                    i7, i8, i9]
                                        # Проверяем, соответствует ли решение условиям головоломки
                                        if is_valid_solution(solution, size):
                                            solutions.append(solution)
                                            # print(solution)
    return solutions




# Функция для вывода решений
def print_solutions(solutions):
    for solution in solutions:
        print_table(solution)
        print('------------')

def print_table(solution):
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
    size = 3
    for i in range(size):
        row = solution[i*size: (i+1)*size]
        row_str = ""
        for cell in row:
            row_str += symbol_map[cell] + " "
        print(row_str)
        if i < size - 1:
            print("    ")



if __name__ == "__main__":
    size = 9
    # Генерируем все возможные решения
    solutions = generate_solutions(size)
    # Выводим решения
    print("Всего решений:", len(solutions))
    print_solutions(solutions)





    # print('1', '\u2510')
    # print('2', '\u250C')
    # print('3', '\u2518')
    # print('4', '\u2514')
    # print('5', '\u2502')
    # print('6', '\u2500')
    # print('7', ' ')