import matplotlib
matplotlib.use('Agg')  # Используем бэкенд Agg
import matplotlib.pyplot as plt



# Функция для чтения данных из файла и возврата списков размеров и времени
def read_file(filename):
    sizes = []
    times = []
    with open("data/"+filename, 'r') as file:
        for line in file:
            if '{' in line and '}' in line:
                data = line.strip('{}\n').split(', ')
                size = int(data[0].split(': ')[1])
                time = float(data[1].split(': ')[1])
                sizes.append(size)
                times.append(time)
    return sizes, times


# Список файлов
files = []

for i in range(1, 9):
    files.append(f'gl-{i}.txt')
print(files)
# Построение графиков
for i, filename in enumerate(files, start=1):
    sizes, times = read_file(filename)

    # Закрыть предыдущую фигуру
    plt.close()

    plt.figure(figsize=(60, 6))
    plt.xticks(ticks=range(min(sizes)-1, max(sizes)+1, 25))
    plt.plot(sizes, times, marker='', linestyle='-')
    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.title(f'Graph {i}')
    plt.grid(True)

    # Сохранение графика в файл
    plt.savefig(f'graphs/graph_{i}.png')

    plt.show()
