def main(text):
    suffixes = [(text[i:], i) for i in range(len(text))]
    print(', '.join([str(i) for _, i in sorted(suffixes)]))


if __name__ == "__main__":
    main('''AACGATAGCGGTAGA$''')

'''
Construct the suffix array of a string.
Given: A string Text.
Return: SuffixArray(Text).
Output:
15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5
'''
