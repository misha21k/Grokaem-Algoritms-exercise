SIMPLE_NUMBER = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23,
                 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 51, 'q': 53, 'r': 61,
                 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 91, 'z': 97}


def hash_1(line):
    return 1


def hash_length(line):
    return len(line)


def hash_first(line):
    return ord(line[0].lower()) - ord('a')


def hash_simple(line):
    sum = 0
    for char in line:
        sum += SIMPLE_NUMBER[char.lower()]
    return sum % 10


if __name__ == '__main__':
    example_5_5 = ['Esther', 'Ben', 'Bob', 'Dan']
    print([hash_1(line) for line in example_5_5])
    print([hash_length(line) for line in example_5_5])
    print([hash_first(line) for line in example_5_5])
    print([hash_simple(line) for line in example_5_5])
    example_5_6 = ['A', 'AA', 'AAA', 'AAAA']
    print([hash_1(line) for line in example_5_6])
    print([hash_length(line) for line in example_5_6])
    print([hash_first(line) for line in example_5_6])
    print([hash_simple(line) for line in example_5_6])
    example_5_7 = ['Maus', 'FunHome', 'Watchmen']
    print([hash_1(line) for line in example_5_7])
    print([hash_length(line) for line in example_5_7])
    print([hash_first(line) for line in example_5_7])
    print([hash_simple(line) for line in example_5_7])