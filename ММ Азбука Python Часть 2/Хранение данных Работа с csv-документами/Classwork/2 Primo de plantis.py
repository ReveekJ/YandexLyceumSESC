import csv

# Открываем файл plantis.csv для записи
with open('plantis.csv', 'w', newline='', encoding='utf-8') as outfile:
    # Создаем объект writer для записи в CSV
    writer = csv.writer(outfile, delimiter=';')

    # Записываем заголовки
    writer.writerow(['nomen', 'definitio', 'pluma', 'Russian nomen', 'familia', 'Russian nomen familia'])

    # Читаем данные о растениях из ввода
    while True:
        try:
            # Считываем строку
            line = input()
            # Убираем лишние пробелы и разделяем по табуляции
            row = line.strip().split('\t')
            # Записываем строку в CSV
            writer.writerow(row)
        except EOFError:
            # Выход из цикла при окончании ввода
            break
