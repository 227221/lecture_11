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


def pattern_search(sequence, letters):
    length = len(letters)
    index = 0
    f = set()
    while sequence:
        if index + length <= len(sequence):
            if sequence[index:index+length] == letters:
                f.add(index)
                index = index + 1
            else:
                index = index + 1
                continue
        else:
            return f


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    dna = read_data("sequential.json", "dna_sequence")
    print(sequential_data)
    number = 5
    outcome = linear_search(sequential_data, number)
    print(outcome)
    letters = "ATA"
    outcome_2 = pattern_search(dna, letters)
    print(outcome_2)


if __name__ == '__main__':
    main()
