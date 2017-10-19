def chromosome_to_cycle(chromosome):
    cycle = []
    for block in chromosome:
        if block > 0:
            cycle.append(2 * block - 1)
            cycle.append(2 * block)
        else:
            cycle.append(- 2 * block)
            cycle.append(- 2 * block - 1)
    return cycle


def create_cycles(chromosomes_as_string):
    chromosomes_as_strings = chromosomes_as_string[1:-1].split(')(')
    cycles = [chromosome_to_cycle(list(map(int, chromosome.split()))) for chromosome in chromosomes_as_strings]
    return cycles


def pairs(cycle):
    for i in range(1, len(cycle) - 1, 2):
        yield '({}, {})'.format(cycle[i], cycle[i + 1])
    yield '({}, {})'.format(cycle[-1], cycle[0])


def colored_edges(cycles):
    return ', '.join(', '.join(pairs(cycle)) for cycle in cycles)


def main():
    chromosomes_as_string = '(+1 -2 -3)(+4 +5 -6)'
    cycles = create_cycles(chromosomes_as_string)
    print(colored_edges(cycles))


if __name__ == '__main__':
    main()

'''
output
(2, 4), (3, 6), (5, 1), (8, 9), (10, 12), (11, 7)
'''
