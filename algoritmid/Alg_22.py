# Проверяет, можно ли разбить список чисел на два подмножества с одинаковой суммой
def can_split_equal_sum_subsets(numbers):
    # Считаем сумму всех чисел
    total_sum = sum(numbers)

    # Если сумма нечётная, то точно нельзя разбить поровну
    if total_sum % 2 != 0:
        return False, [], []

    # Целевая сумма для каждого подмножества
    target_sum = total_sum // 2

    # Функция, которая с помощью перебора ищет подмножество с нужной суммой
    def backtrack(start_index, curr_sum, curr_subset):
        # Если сумма совпала — подмножество найдено
        if curr_sum == target_sum:
            return True, curr_subset
        # Пробуем добавить в подмножество следующие числа
        for i in range(start_index, len(numbers)):
            if curr_sum + numbers[i] <= target_sum:
                result, subset = backtrack(i + 1, curr_sum + numbers[i], curr_subset + [numbers[i]])
                if result:
                    return True, subset
        return False, []

    # Ищем первое подмножество с нужной суммой
    result, subset1 = backtrack(0, 0, [])

    if result:
        # Находим оставшиеся элементы — они образуют второе подмножество
        used = subset1.copy()
        subset2 = []
        for num in numbers:
            if num in used:
                used.remove(num)
            else:
                subset2.append(num)
        return True, subset1, subset2
    else:
        return False, [], []

# Пример использования функции
numbers = [1, 2, 3, 4, 5, 6, 7]
# Сортируем для удобства (это не обязательно, но может ускорить поиск)
numbers.sort()

result, subset1, subset2 = can_split_equal_sum_subsets(numbers)

if result:
    print("Первое подмножество:", subset1)
    print("Второе подмножество:", subset2)
else:
    print("Невозможно разделить множество на два подмножества с равными суммами.")
