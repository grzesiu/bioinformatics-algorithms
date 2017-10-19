def get_edge(edges, i, j):
    if (i, j) in edges:
        return i, j
    else:
        return j, i


def replace(edges, old, new):
    edges.remove(old)
    edges.append(new)


def main():
    edges = [(2, 4), (3, 8), (7, 5), (6, 1)]
    indices = [1, 6, 3, 8]

    i, ip = get_edge(edges, indices[0], indices[1])
    j, jp = get_edge(edges, indices[2], indices[3])

    replace(edges, (i, ip), (i, j))
    replace(edges, (j, jp), (ip, jp))

    print(', '.join(map(str, edges)))


if __name__ == '__main__':
    main()

'''
output
(2, 4), (7, 5), (6, 3), (1, 8)
'''
