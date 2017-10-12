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


def main():
    chromosome_as_string = '(+1 -2 -3 +4)'
    chromosome = list(map(int, chromosome_as_string[1:-1].split()))
    cycle = chromosome_to_cycle(chromosome)

    print('({:s})'.format(' '.join(map(str, cycle))))


if __name__ == '__main__':
    main()

'''
output
(1 2 4 3 6 5 7 8)
'''
