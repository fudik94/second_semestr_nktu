def radix_sort(arr):
    # Создаем 10 корзин для цифр 0-9
    buckets = [[] for _ in range(10)]

    # Сортируем по единичным разрядам
    for num in arr:
        digit_val = num % 10
        buckets[digit_val].append(num)
    
    # Собираем числа обратно в массив
    arr = [num for bucket in buckets for num in bucket]
    # Очищаем корзины
    buckets = [[] for _ in range(10)]

    # Сортируем по десяткам
    for num in arr:
        digit_val = (num // 10) % 10
        buckets[digit_val].append(num)
    
    # Собираем числа обратно в массив
    arr = [num for bucket in buckets for num in bucket]
    # Очищаем корзины
    buckets = [[] for _ in range(10)]

    # Сортируем по сотням
    for num in arr:
        digit_val = (num // 100) % 10
        buckets[digit_val].append(num)

    # Собираем числа обратно в массив
    arr = [num for bucket in buckets for num in bucket]

    return arr

# Пример использования
arr = [170, 454, 775, 900, 802, 244, 254, 666]
sorted_arr = radix_sort(arr)
print("Отсортированный массив:", sorted_arr)
