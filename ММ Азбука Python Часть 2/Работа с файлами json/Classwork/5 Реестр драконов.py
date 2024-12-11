import csv
import json


def main():
    dragons_list = []

    with open("dragons.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dragon = {
                "name": row["name"],
                "place": row["place"],
                "nature": row["nature"],
                "number_of_heads": row["number_of_heads"],
                "possession_of_the_true_speech": row["possession_of_the_true_speech"]
            }
            dragons_list.append(dragon)

    output_data = {"dragons": dragons_list}

    with open("dragons.json", "w", encoding="utf-8") as jsonfile:
        json.dump(output_data, jsonfile, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()