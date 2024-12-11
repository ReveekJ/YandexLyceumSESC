def sum_of_multiples(N, divisors):
    total_sum = 0
    for i in range(N):
        if any(i % d == 0 for d in divisors):
            total_sum += i
    return total_sum


def main():
    with open("data.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        N = int(lines[0].strip())
        divisors = list(map(int, lines[1].strip().split()))

    result = sum_of_multiples(N, divisors)

    print(result)


if __name__ == "__main__":
    main()
