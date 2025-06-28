def hamming_distance(str1, str2):
    # Проверяем, что строки одинаковой длины
    if len(str1) != len(str2):
        raise ValueError("Строки должны быть одинаковой длины.")
    
    # Считаем количество различий
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    
    return distance

# Пример использования
str1 = "karolin"
str2 = "kathrin"
try:
    result = hamming_distance(str1, str2)
    print(f"Расстояние Хэмминга между строками: {result}")
except ValueError as e:
    print(e)
