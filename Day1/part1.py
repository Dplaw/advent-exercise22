def main():
    data = get_data()
    result = elf_most_calories(data)
    return result


def get_data():
    with open('adv.txt', mode='r') as file:
        data = file.read()
    return [grp.split("\n") for grp in data.split("\n\n")]


def elf_most_calories(calories_pack):
    return max([sum([int(s) for s in cal]) for cal in calories_pack])


if __name__ == "__main__":
    m = main()
    print(m)