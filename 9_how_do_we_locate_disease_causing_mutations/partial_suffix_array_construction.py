def main(data_as_string):
    text, k = data_as_string.split()
    k = int(k)
    suffixes = [(text[i:], i) for i in range(len(text))]
    suffix_array = [i for _, i in sorted(suffixes)]
    partial_suffix_array = filter(lambda x: not x[1] % k, enumerate(suffix_array))
    for (i, sai) in partial_suffix_array:
        print('{},{}'.format(i, sai))


if __name__ == "__main__":
    main('''PANAMABANANAS$
5''')

'''
Construct the partial suffix array of a string.
Given: A string Text and a positive integer K.
Return: SuffixArrayK(Text), in the form of a list of ordered pairs (i, SuffixArray(i)) for all nonempty entries in the partial suffix array.
Output:
1,5
11,10
12,0
'''
