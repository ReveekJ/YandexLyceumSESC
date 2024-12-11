import csv
import sys
n, m = map(int, input(). split())
a = sys. stdin. readlines()
d = []
for i in a:
    i = i. rstrip()
    i = i. split()
    if int(i[2]) + int(i[3]) + int(i[4]) >= n and min(int(i[2]), int(i[3]), int(i[4])) >= m:
        d. append(i + [int(i[2]) + int(i[3]) + int(i[4])])
with open('exam.csv', 'w') as csvfile:
    writer = csv. writer(
        csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer. writerow(['Фамилия', 'имя', 'результат 1', 'результат 2', 'результат 3', 'сумма'])
    for i in d:
        writer.writerow(i)
