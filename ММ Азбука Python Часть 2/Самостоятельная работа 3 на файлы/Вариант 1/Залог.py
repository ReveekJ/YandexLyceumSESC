import csv
import math

# Чтение необходимых данных из стандартного ввода
required_sum, max_quantity = map(int, input().split())

# Чтение данных из файла pledge.csv
pledge_data = []
with open('pledge.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        pledge_data.append(row)

# Список для хранения подходящих вещей
suitable_items = []

# Обработка данных
for item in pledge_data:
    quantity = int(item['quantity'])
    cost = int(item['cost'])
    wear = float(item['wear'])

    # Вычисление общей стоимости с учетом износа
    total_cost = quantity * cost * (1 - wear)
    total_cost = math.floor(total_cost)  # Округление вниз

    # Проверка условий
    if total_cost >= required_sum and quantity <= max_quantity:
        suitable_items.append({
            'thing': item['thing'],
            'quantity': quantity,
            'total_cost': total_cost
        })

# Сортировка по общей стоимости, затем по имени вещи
suitable_items.sort(key=lambda x: (x['total_cost'], x['thing']))

# Запись результата в файл deposit.csv
with open('deposit.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=':', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['thing', 'quantity', 'total cost'])  # Заголовки
    for item in suitable_items:
        writer.writerow([item['thing'], item['quantity'], item['total_cost']])
