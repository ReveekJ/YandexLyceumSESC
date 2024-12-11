def love_or_not(starting_phrase, petals):
    phrases = ["любит", "не любит"]
    current_index = phrases.index(starting_phrase)

    for _ in range(petals):
        current_index = 1 - current_index

    result = phrases[(current_index + 1) % 2]

    with open("fortune.txt", "w", encoding="utf-8") as file:
        file.write(result)


starting_phrase = input().strip().lower()
petals = int(input().strip())

love_or_not(starting_phrase, petals)