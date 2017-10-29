def last_to_first(first_indices, position):
    for i in range(len(first_indices)):
        if first_indices[i][1] == position:
            return i


def count_matches(first_indices, last_symbols, pattern):
    top_first = 0
    bottom_first = len(last_symbols) - 1
    while top_first <= bottom_first:
        if pattern:
            pattern, symbol = pattern[:-1], pattern[-1]
            top_last = last_symbols[top_first:bottom_first + 1].find(symbol) + top_first
            bottom_last = last_symbols[top_first:bottom_first + 1].rfind(symbol) + top_first

            if top_last >= top_first and bottom_last >= top_first:
                top_first = first_indices.index(top_last)
                bottom_first = first_indices.index(bottom_last)
            else:
                return 0
        else:
            return bottom_first - top_first + 1


def get_first_indices(last_symbols):
    last_enum = [(v, i) for i, v in enumerate(last_symbols)]
    _, first_indices = zip(*sorted(last_enum))
    return first_indices


def main(data_as_string):
    last_symbols, *patterns = data_as_string.split()
    first_indices = get_first_indices(last_symbols)
    for pattern in patterns:
        print(count_matches(first_indices, last_symbols, pattern), end=' ')


if __name__ == "__main__":
    main('''TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC
CCT CAC GAG CAG ATC''')

'''
Given: A string BWT(Text), followed by a collection of strings Patterns.
Return: A list of integers, where the i-th integer corresponds to the number of substring matches of the i-th member of Patterns in Text.
Output:
2 1 1 0 1
'''
