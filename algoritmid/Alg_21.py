def get_ratio(item):
    # Считаем, сколько стоит один килограмм предмета
    weight, value = item
    return value / weight

def knapsack_brute_force(items, capacity):
    # Подбираем лучшую комбинацию предметов, перебирая все варианты
    n = len(items)
    max_value = 0

    # Перебираем все возможные наборы предметов
    for i in range(2 ** n):
        total_weight = 0
        total_value = 0
        for j in range(n):
            if (i >> j) & 1:
                total_weight += items[j][0]
                total_value += items[j][1]
                # Если слишком тяжело — прекращаем проверку этого набора
                if total_weight > capacity:
                    break
        # Если набор помещается и стоит дороже предыдущих — запоминаем его
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value

    return max_value

# Пример предметов: (вес, цена)
items = [(2, 3), (3, 4), (4, 5), (1, 6), (1, 7)]

# Сколько рюкзак может унести
capacity = 10

# Сортируем предметы по выгодности (цена за килограмм)
items.sort(key=get_ratio, reverse=True)

# Вызываем функцию и выводим результат
max_value = knapsack_brute_force(items, capacity)
print("Максимальная суммарная стоимость предметов в рюкзаке:", max_value)
