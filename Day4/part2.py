import re


def main():
    data = get_data()
    my_func = get_scopes
    result = get_result(data, my_func)
    print(result)


def get_data():
    with open('data.txt', mode='r') as file:
        data = file.read()
    return [[int(i) for i in re.findall(r'\d+', line)]
            for line in data.splitlines()]


def get_scopes(pairs):
    if pairs[1] >= pairs[2] and pairs[0] <= pairs[3]:
        return True
    else:
        return False


def get_result(data, func):
    return sum([func(item) for item in data])


if __name__ == '__main__':
    main()
