
def main():
    data = get_data()
    my_func = partial_result
    results = get_result(data, my_func)
    return results


def get_data():
    with open('data.txt', mode='r') as file:
        data = [line.replace('\n', '').split(' ')
                for line in file]
    return data


def partial_result(operator):
    return {
        ('A', 'X'): lambda: 1+3,
        ('B', 'Y'): lambda: 2+3,
        ('C', 'Z'): lambda: 3+3,
        ('A', 'Y'): lambda: 2+6,
        ('A', 'Z'): lambda: 3+0,
        ('B', 'X'): lambda: 1+0,
        ('B', 'Z'): lambda: 3+6,
        ('C', 'X'): lambda: 1+6,
        ('C', 'Y'): lambda: 2+0,
    }.get(operator, lambda: None)()


def get_result(data, my_dict):
    return sum([my_dict(tuple(i)) for i in data])
    
    
if __name__ == '__main__':
    print(main())