with open('borsch.txt') as file:
    a, b, c = map(float, file.readlines())


def price(x, y, z):
    print(x * a + y * b + z * c)
