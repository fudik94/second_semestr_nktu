import time
import random
import matplotlib.pyplot as plt

def binary_search(arr, target):
    # Бинарный поиск в отсортированном массиве.
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def test_binary_search(arr, target):
    # Тестирование бинарного поиска.
    start_time = time.time()
    time.sleep(2)  # Задержка для отображения времени работы
    result = binary_search(arr, target)
    end_time = time.time()
    print("Размер массива:", len(arr), "Время:", end_time - start_time)
    return end_time - start_time

# Цель поиска
target = 1
# Тестирование для разных размеров массивов
sizes = [1000, 5000, 10000, 20000, 50000]
times = []

for size in sizes:
    data = sorted(random.sample(range(size * 10), size))
    time_taken = test_binary_search(data, target)
    times.append(time_taken)

# Построение графика
plt.plot(sizes, times, marker='o')
plt.title('Время бинарного поиска в зависимости от размера массива')
plt.xlabel('Размер массива')
plt.ylabel('Время (сек)')
plt.grid(True)
plt.show()
