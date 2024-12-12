with open('holes.txt', 'r') as file, open('glasses.txt', 'w') as output:
    for line in file.readlines():
        eye, holes = line.split()[0], line.split()[1:]
        output.write(str(max(0, max(list(map(int, holes))) - int(eye))) + '\n')
