import os
import json


# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None
    else:
        file_path = os.path.join(cwd_path, file_name)
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
    return data[field]


def linear_search(sequence, number):
    positions = []
    count = 0
    for index, unit in enumerate(sequence):
        if unit == number:
            positions.append(index)
            count = count + 1
        else:
            continue
    field = {"positions": positions, "count": count}
    return field


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    number = 5
    outcome = linear_search(sequential_data, number)
    print(outcome["positions"])
    print(outcome["count"])
    print(outcome)


if __name__ == '__main__':
    main()
