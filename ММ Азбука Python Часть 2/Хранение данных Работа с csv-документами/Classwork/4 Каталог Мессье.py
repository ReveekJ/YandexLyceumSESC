import csv

# Открываем файл messier.txt для чтения
with open('messier.txt', 'r', encoding='utf-8') as infile:
    # Читаем строки из файла
    lines = infile.readlines()

# Открываем файл messier.csv для записи
with open('messier.csv', 'w', newline='', encoding='utf-8') as outfile:
    # Создаем объект writer для записи в CSV
    writer = csv.writer(outfile, delimiter=';')

    # Проходим по всем строкам и записываем их в CSV
    for line in lines:
        # Убираем символы новой строки и разделяем по табуляции
        row = line.strip().split('\t')
        # Записываем строку в CSV
        writer.writerow(row)
