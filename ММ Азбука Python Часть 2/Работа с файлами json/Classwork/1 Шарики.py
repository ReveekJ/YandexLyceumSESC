import json
import math


# Загрузить данные из файла
with open('input.json', 'r') as file:
    data = json.load(file)


# Функция для вычисления расстояния от начала координат
def distance_from_origin(ball):
    return math.sqrt(ball['x']**2 + ball['y']**2)


# Сортировка по количеству цветов, радиусу, расстоянию от начала координат и id
sorted_balls = sorted(data, key=lambda ball: (-len(ball['colors']), -ball['radius'], -distance_from_origin(ball),
                                              ball['id']))

# Вывод id шариков в требуемом порядке
sorted_ids = [ball['id'] for ball in sorted_balls]
print(*sorted_ids)
