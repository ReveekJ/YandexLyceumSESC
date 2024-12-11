import json


def create_word_dict():
    word_dict = {}

    with open('russian_words.txt', 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if word:  # Проверяем, что строка не пустая
                first_letter = word[0].lower()  # Приводим к нижнему регистру
                if first_letter not in word_dict:
                    word_dict[first_letter] = []
                word_dict[first_letter].append(word)

    with open('russian_words.json', 'w', encoding='utf-8') as json_file:
        json.dump(word_dict, json_file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    create_word_dict()
