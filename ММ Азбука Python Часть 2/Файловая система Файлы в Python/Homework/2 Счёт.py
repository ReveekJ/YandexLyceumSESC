def find_winners(input_filename):
    scores = {}

    with open(input_filename, 'r', encoding='utf-8') as file:
        for line in file:
            nickname, score = line.strip().split(': ')
            score = int(score)
            if nickname in scores:
                scores[nickname] += score
            else:
                scores[nickname] = score

    max_score = max(scores.values())
    winners = sorted([nickname for nickname, score in scores.items() if score == max_score])

    print('\n'.join(winners))


input_filename = 'rating.txt'
find_winners(input_filename)
