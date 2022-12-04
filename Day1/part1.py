def main():
    data = get_data()
    result = get_most_caloric_pack(data)
    print(result)


def get_data():
    with open('adv.txt', mode='r') as file:
        data = file.read()
    return [grp.split("\n") for grp in data.split("\n\n")]


def get_most_caloric_pack(packs):
    calories_per_pack = [
        sum([int(cal) for cal in pack])
        for pack in packs
    ]
    return max(calories_per_pack)


if __name__ == "__main__":
    main()