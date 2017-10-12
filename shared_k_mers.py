from collections import defaultdict

complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}


def find(k_mers, k_mer, j):
    if k_mer in k_mers:
        for i in k_mers[k_mer]:
            print('({:d}, {:d})'.format(i, j))


def reverse(k_mer):
    return ''.join(complement[x] for x in reversed(k_mer))


def main():
    k = 3
    s1 = 'AAACTCATC'
    s2 = 'TTTCAAATC'
    k_mers = defaultdict(list)
    for i in range(len(s1) - k + 1):
        k_mers[s1[i:i + k]].append(i)

    for j in range(len(s2) - k + 1):
        find(k_mers, s2[j:j + k], j)
        find(k_mers, reverse(s2[j:j + k]), j)


if __name__ == '__main__':
    main()

'''
output
(0, 0)
(4, 2)
(0, 4)
(6, 6)
'''
