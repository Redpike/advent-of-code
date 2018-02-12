import json


part = 0


def read_input_file():
    return json.load(open('input', 'r'))


def sum_of_objects(json_data):
    if type(json_data) is int:
        return json_data

    elif type(json_data) is list:
        return sum(map(sum_of_objects, json_data))

    elif type(json_data) is dict:
        values = json_data.values()

        if part == 2 and 'red' in values:
            return 0

        return sum(map(sum_of_objects, values))
    else:
        return 0


def main():
    json_data = read_input_file()
    global part
    part = 1
    print('Day 12 Part 1:', sum_of_objects(json_data))
    part = 2
    print('Day 12 Part 2:', sum_of_objects(json_data))


if __name__ == '__main__':
    main()
