import string


def main():
    data = get_data()
    numbers = get_numbers()
    my_func = get_the_repetition
    result = get_result(data, my_func, numbers)
    print(result)


def get_data():
    with open('data.txt', mode='r') as file:
        data = file.read()
    split_data = data.split("\n")
    return [split_data[index:index+3]
            for index in range(0, len(split_data), 3)]


def get_numbers():
    return {letter: number
                for number, letter in
                enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1)}


def get_the_repetition(my_data):
    return [[i for i in rucksack[0]
             if i in rucksack[1] and i in rucksack[2]]
            for rucksack in my_data]


def get_result(data, my_func, my_dict):
    return sum([my_dict[i[0]] for i in  my_func(data)])


if __name__ == '__main__':
    main()
