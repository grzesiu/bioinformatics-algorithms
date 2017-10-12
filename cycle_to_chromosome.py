def cycle_to_chromosome(cycle):
    return [block // 2 + 1 if block % 2 else -block // 2 for block in cycle[::2]]


def main():
    cycle_as_string = '(1 2 4 3 6 5 7 8)'
    cycle = list(map(int, cycle_as_string[1:-1].split()))
    chromosome = cycle_to_chromosome(cycle)

    chromosome_as_string = ['{0:+d}'.format(block) for block in chromosome]
    print('({:s})'.format(' '.join(chromosome_as_string)))


if __name__ == '__main__':
    main()

'''
output
(+1 -2 -3 +4)
'''
