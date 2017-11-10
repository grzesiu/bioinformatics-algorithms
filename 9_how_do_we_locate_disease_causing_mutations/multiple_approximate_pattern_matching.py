from heapq import merge


def last_to_first(first_indices, position):
    for i in range(len(first_indices)):
        if first_indices[i][1] == position:
            return i


def get_matches(mapping, last_symbols, pattern, d):
    mismatches = [0] * len(last_symbols)
    while pattern:
        pattern, symbol = pattern[:-1], pattern[-1]

        for i in range(len(last_symbols)):
            if last_symbols[i] != symbol:
                mismatches[i] += 1

        _, mismatches = zip(*sorted(zip(mapping, mismatches)))
        mismatches = list(mismatches)

    return [i for i in range(len(mismatches)) if mismatches[i] <= d]


def get_mapping(last_symbols):
    last = [(v, i) for i, v in enumerate(last_symbols)]
    first = [(v, i) for i, v in enumerate(sorted(last_symbols))]
    last_sorted = sorted(last)
    mapping = [(last_sorted[i][1], first[i][1]) for i in range(len(last_symbols))]
    _, mapping = zip(*sorted(mapping))
    return mapping


def transform(text):
    cyclic_rotations = [text[i:] + text[:i] for i in range(len(text))]
    bwt = [cyclic_rotation[-1] for cyclic_rotation in sorted(cyclic_rotations)]
    return ''.join(bwt)


def create_suffix_array(text):
    suffixes = [(text[i:], i) for i in range(len(text))]
    return [i for _, i in sorted(suffixes)]


def get_all_matches(text, patterns, d):
    last_symbols = transform(text)
    mapping = get_mapping(last_symbols)
    matches = [get_matches(mapping, last_symbols, pattern, d) for pattern in patterns]
    return list(merge(*matches))


def get_starting_positions(text, patterns, d):
    suffix_array = create_suffix_array(text)
    matches = get_all_matches(text, patterns, d)
    starting_positions = [suffix_array[match] for match in matches]
    return sorted(starting_positions)


def main(data_as_string):
    text, patterns, d = data_as_string.split('\n')
    d = int(d)
    patterns = patterns.split()
    print(' '.join(map(str, get_starting_positions(text, patterns, d))))


if __name__ == "__main__":
    main('''ACATGCTACTTT$
ATT GCC GCTA TATT
1''')

'''
Find all approximate occurrences of a collection of patterns in a text.
Given: A string Text, a collection of strings Patterns, and an integer d.
Return: All positions in Text where a string from Patterns appears as a substring with at most d mismatches.
Output:
2 4 4 6 7 8 9
'''
