import string


def main():
    data = get_data()
    numbers = get_numbers()
    repeat = get_the_repetition
    result = get_result(data, repeat, numbers)
    print(result)


def get_data():
    with open('data.txt', mode='r') as file:
        data = file.read()
    return [line for line in data.split("\n")]


def get_numbers():
    return {letter: number
                for number, letter in
                enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1)}


def get_the_repetition(rucksack):
    return [i for i in rucksack[:len(rucksack)//2]
            if i in rucksack[len(rucksack)//2:]]


def get_result(data, my_func, my_dict):
    return sum([my_dict[(my_func(rucksack)[0])]
            for rucksack in data])


if __name__ == '__main__':
    main()
