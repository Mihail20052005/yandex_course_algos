def count_cubes(N, M, cubes):
    # Создаем словарь для отслеживания цветов кубиков
    color_count = {}

    # Создаем список для подсчета кубиков, видимых в зеркале
    mirror_visible = [0] * N

    # Инициализируем переменную для подсчета видимых кубиков
    visible_count = 0

    # Перебираем кубики справа налево
    for i in range(N - 1, -1, -1):
        color = cubes[i]
        if color not in color_count:
            color_count[color] = 1
            visible_count += 1
        else:
            color_count[color] += 1

        mirror_visible[i] = visible_count

    # Перебираем кубики слева направо, подсчитывая возможные значения K
    possible_k_values = []
    current_color_count = {}
    current_visible_count = 0

    for i in range(N - 1):
        color = cubes[i]
        if color not in current_color_count:
            current_color_count[color] = 1
            current_visible_count += 1
        else:
            current_color_count[color] += 1

        if current_visible_count == mirror_visible[i + 1]:
            possible_k_values.append(i + 1)

    return possible_k_values


# Чтение входных данных
N, M = map(int, input().split())
cubes = list(map(int, input().split()))

# Вызываем функцию и выводим результат
result = count_cubes(N, M, cubes)
print(*result)
