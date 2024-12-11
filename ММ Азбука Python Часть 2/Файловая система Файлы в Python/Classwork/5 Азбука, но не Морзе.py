import sys

with open(input()) as file:
    a = {line.split()[1].strip(): line.split()[0].strip() for line in file.readlines()}

codes = sys.stdin.readlines()

with open('result.txt', 'w') as file:
    for code in codes:
        word = ''
        for letter in code.split():
            word += a[letter]
        file.write(word + '\n')
