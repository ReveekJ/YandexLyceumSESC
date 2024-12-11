import csv

# Ввод года
year = input()

# Инициализация переменных
top_youtubers = []
unique_categories = set()

# Чтение данных из CSV файла
with open('top_youtube_channels_data.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    # Фильтрация данных по году
    for row in reader:
        if row['started'] == year:
            # Добавление в список для топ-3
            top_youtubers.append(row)
            # Добавление подписчиков
            # total_subscribers += int(row['subscribers'])
            # Добавление категории в множество
            unique_categories.add(row['category'])

# Сортировка по rank и получение топ-3
top_youtubers.sort(key=lambda x: int(x['rank']))
top_3 = top_youtubers[:3]

# Формирование вывода
top_youtubers_names = ', '.join([youtuber['youtuber'] for youtuber in top_3])
unique_categories_list = '; '.join(unique_categories)
total_subscribers = 0

for i in top_3:
    total_subscribers += int(i['subscribers'])

# Вывод результатов
print(top_youtubers_names)
print(total_subscribers)
print(unique_categories_list)
