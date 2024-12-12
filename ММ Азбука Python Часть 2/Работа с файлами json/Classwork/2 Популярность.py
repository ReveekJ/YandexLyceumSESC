import json

a = input()
b = input()
d = {}

with open(a, encoding='utf8') as inp:
    data = json.load(inp)
    for i in data:
        if i[b] in d.keys():
            d[i[b]].append(i['youtuber'])
        else:
            d[i[b]] = [i['youtuber']]
    print(d)
