def main(data_as_string):
    text, *patterns = data_as_string.split()
    suffix_array = [(text[i:], i) for i in range(len(text))]
    starting_positions = [i for suffix, i in suffix_array for p in patterns if suffix.startswith(p)]
    print(' '.join(map(str, sorted(starting_positions))))


if __name__ == "__main__":
    main('''AATCGGGTTCAATCGGGGT
ATCG
GGGT''')

'''
Given: A string Text and a collection of strings Patterns.
Return: All starting positions in Text where a string from Patterns appears as a substring.
Output:
1 4 11 15
'''
