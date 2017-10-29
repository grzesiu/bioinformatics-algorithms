import itertools
import operator


def last_to_first(first_indices, position):
    for i in range(len(first_indices)):
        if first_indices[i][1] == position:
            return i


def get_matches(first_indices, last_symbols, pattern):
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
                return []
        else:
            return list(range(top_first, bottom_first + 1))


def get_first_indices(last_symbols):
    last_enum = [(v, i) for i, v in enumerate(last_symbols)]
    _, first_indices = zip(*sorted(last_enum))
    return first_indices


def transform(text):
    cyclic_rotations = [text[i:] + text[:i] for i in range(len(text))]
    bwt = [cyclic_rotation[-1] for cyclic_rotation in sorted(cyclic_rotations)]
    return ''.join(bwt)


def create_suffix_array(text):
    suffixes = [(text[i:], i) for i in range(len(text))]
    return [i for _, i in sorted(suffixes)]


def get_all_matches(text, patterns):
    last_symbols = transform(text)
    first_indices = get_first_indices(last_symbols)
    matches = [get_matches(first_indices, last_symbols, pattern) for pattern in patterns]
    return list(itertools.chain.from_iterable(matches))


def get_starting_positions(text, patterns):
    text += '$'
    suffix_array = create_suffix_array(text)
    matches = get_all_matches(text, patterns)
    return sorted(operator.itemgetter(*matches)(suffix_array))


def main(data_as_string):
    text, *patterns = data_as_string.split()
    print(' '.join(map(str, get_starting_positions(text, patterns))))


if __name__ == "__main__":
    main('''AATCGGGTTCAATCGGGGT
ATCG
GGGT''')

'''
Find all occurrences of a collection of patterns in a text.
Given: A string Text and a collection of strings Patterns.
Return: All starting positions in Text where a string from Patterns appears as a substring.
Output:
1 4 11 15
'''
