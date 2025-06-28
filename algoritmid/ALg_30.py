def k_means_clustering(points, k, max_iterations):
    # Инициализация центров кластеров
    xmin = min(points)  
    xmax = max(points)  
    cluster_centers = [xmin + i * (xmax - xmin) / (k - 1) for i in range(k)]

    for _ in range(max_iterations):
        # Присваиваем точки кластерам
        clusters = [[] for _ in range(k)]
        for point in points:
            distances = [abs(point - center) for center in cluster_centers]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(point)

        # Обновляем центры кластеров
        new_centers = [sum(cluster) / len(cluster) if cluster else cluster_centers[i] for i, cluster in enumerate(clusters)]

        # Проверка на сходимость
        if new_centers == cluster_centers:
            break
        cluster_centers = new_centers

    # Повторно распределяем точки по кластерам с использованием финальных центров
    clusters = [[] for _ in range(k)]
    for point in points:
        distances = [abs(point - center) for center in cluster_centers]
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)

    # Создаем список с данными о кластерной принадлежности точек
    cluster_assignments = []
    for point in points:
        for i, cluster in enumerate(clusters):
            if point in cluster:
                cluster_assignments.append(i)
                break

    return cluster_assignments, cluster_centers

# Пример использования
points = [1, 2, 3, 6, 7, 8, 10, 11, 14, 15]
k = 3
max_iterations = 100
cluster_assignments, cluster_centers = k_means_clustering(points, k, max_iterations)

print("Кластерные принадлежности:", cluster_assignments)
print("Центры кластеров:", cluster_centers)
