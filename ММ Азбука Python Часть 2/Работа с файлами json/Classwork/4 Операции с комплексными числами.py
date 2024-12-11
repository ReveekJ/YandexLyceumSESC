import json


def add_complex(c1, c2):
    return {"Re": c1["Re"] + c2["Re"], "Im": c1["Im"] + c2["Im"]}


def subtract_complex(c1, c2):
    return {"Re": c1["Re"] - c2["Re"], "Im": c1["Im"] - c2["Im"]}


def multiply_complex(c1, c2):
    return {"Re": c1["Re"] * c2["Re"] - c1["Im"] * c2["Im"], "Im": c1["Re"] * c2["Im"] + c1["Im"] * c2["Re"]}


with open('in.json', 'r') as file:
    data = json.load(file)['complex']

c1 = data[0]
c2 = data[1]

result_sum = add_complex(c1, c2)
result_difference = subtract_complex(c1, c2)
result_product = multiply_complex(c1, c2)

output_data = {"complex": [result_sum, result_difference, result_product]}

with open("out.json", "w", encoding="utf-8") as outfile:
    json.dump(output_data, outfile, ensure_ascii=False, indent=4)
