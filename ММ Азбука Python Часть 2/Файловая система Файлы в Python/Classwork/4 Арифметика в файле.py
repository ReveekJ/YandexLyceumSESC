with open('in_file.txt') as inp, open('out_file.txt', 'w') as output:
    res = []
    for i in inp.readlines():
        res.append(f'{i.strip()} = {eval(i.strip())}\n')

    output.writelines(res)
