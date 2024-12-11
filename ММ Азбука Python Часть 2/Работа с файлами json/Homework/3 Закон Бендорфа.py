import json


def calculate_first_digit_probabilities():
    first_digit_count = {}
    total_count = 0

    with open('input.txt', 'r') as file:
        for line in file:
            number = line.strip()
            if number:  # Проверяем, что строка не пустая
                first_digit = number[0]
                if first_digit in first_digit_count:
                    first_digit_count[first_digit] += 1
                else:
                    first_digit_count[first_digit] = 1
                total_count += 1

    probabilities = {digit: (count / total_count) * 100 for digit, count in first_digit_count.items()}

    with open('output.json', 'w') as json_file:
        json.dump(probabilities, json_file, indent=2)


if __name__ == "__main__":
    calculate_first_digit_probabilities()
