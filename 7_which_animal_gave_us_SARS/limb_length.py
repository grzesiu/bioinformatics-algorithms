import math


def limb_length(n, j, dist):
    min_ll = math.inf
    i = j - 2 * (j > 0) + 1
    for k in range(n):
        if k != j and k != i:
            cur_ll = (dist[i][j] + dist[j][k] - dist[i][k]) // 2
            min_ll = min(min_ll, cur_ll)

    return min_ll


def parse(distances_as_string):
    distances = []
    for row in distances_as_string.splitlines():
        distances.append(list(map(int, row.split())))
    return distances


def main():
    n = 4
    j = 1
    distances_as_string = '''0   13  21  22
13  0   12  13
21  12  0   13
22  13  13  0'''

    distances = parse(distances_as_string)
    print(limb_length(n, j, distances))


if __name__ == '__main__':
    main()

'''
Find the limb length for a leaf in a tree.
Given: An integer n, followed by an integer j between 0 and n - 1, followed by a space-separated additive distance matrix D (whose elements are integers).
Return: The limb length of the leaf in Tree(D) corresponding to row j of this distance matrix (use 0-based indexing).
Output: 
2
'''
