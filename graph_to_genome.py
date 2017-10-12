import re


def cycle_to_chromosome(cycle):
    return [-(block // 2 + 1) if block % 2 else block // 2 for block in cycle[::2]]


def is_end(cycle):
    def is_end_in_outgoing():
        return cycle[0] == cycle[-1] - 1

    def is_end_in_ingoing():
        return cycle[0] == cycle[-1] + 1

    if cycle:
        return is_end_in_outgoing() if cycle[0] % 2 else is_end_in_ingoing()
    return False


def from_str(edges_as_string):
    vertices = list(map(int, re.findall(r'\d+', edges_as_string)))
    i = 0
    cycle = []
    while i < len(vertices):
        cycle.append(vertices[i])
        if is_end(cycle):
            yield cycle
            cycle = []
        i += 1


def main():
    edges_as_string = '(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)'

    for cycle in from_str(edges_as_string):
        print('({})'.format(' '.join(map('{0:+}'.format, cycle_to_chromosome(cycle)))), end='')


if __name__ == '__main__':
    main()

'''
output
(+1 -2 -3)(-4 +5 -6)
'''
