import csv

n = input()
a, b = map(int, input().split())

with open('salary.csv', encoding="utf8") as mt, open('out_file.csv', 'w', encoding="utf8") as csvf:
    data = csv.DictReader(mt, delimiter=';', quotechar='"')
    writer = csv.writer(csvf, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    r = list(filter(lambda x: x['Федеральный округ'] == n, data))
    r1 = list(filter(lambda x: int(x[str(b)]) / int(x[str(a)]) < 1.04, r))
    if r1 != []:
        writer.writerow(['Субъект', a, b])
    for i in r1:
        writer.writerow([i['Субъект'], i[str(a)], i[str(b)]])
