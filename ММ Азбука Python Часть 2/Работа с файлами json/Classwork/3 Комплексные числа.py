
import json
import re
import sys


def parse_complex_number(input_string):
    pattern = r"z\s*=\s*([+-]?\d*\.?\d*)\s*([+-]?\s*\d*\.?\d*)\s*\*\s*i"
    match = re.match(pattern, input_string.replace(" ", ""))

    if match:
        re_part = float(match.group(1))
        im_part = float(match.group(2).replace(" ", ""))
        return {"Re": re_part, "Im": im_part}
    else:
        return None


def main():
    complex_numbers = []

    strings = sys.stdin.readlines()
    for input_string in strings:
        complex_number = parse_complex_number(input_string)
        complex_numbers.append(complex_number)

    output_data = {"complex": complex_numbers}

    with open("output.json", "w", encoding="utf-8") as file:
        json.dump(output_data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()

