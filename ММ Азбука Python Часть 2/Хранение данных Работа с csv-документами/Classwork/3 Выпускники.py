import csv


def filter_specialties(min_percentage):
    with open('vps.csv', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Пропускаем заголовок
        specialties = []

        for row in reader:
            specialty = row[0]
            corresponds_percentage = int(row[4])  # Соответствует в %

            if corresponds_percentage >= min_percentage:
                specialties.append(specialty)

    return specialties


if __name__ == "__main__":
    min_percentage = int(input())
    result = filter_specialties(min_percentage)

    for specialty in result:
        print(specialty)


