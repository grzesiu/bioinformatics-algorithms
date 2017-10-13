class Genome:
    def __init__(self, al, not_visited):
        self.al = al
        self.not_visited = not_visited

    def __getitem__(self, item):
        return self.al[item]

    def __setitem__(self, key, value):
        self.al[key] = value

    @classmethod
    def from_string(cls, genome_as_string):
        chromosomes = [list(map(int, c.split())) for c in genome_as_string[1:-1].split(')(')]

        al = {}
        not_visited = []

        def add(x, y):
            al[x] = y
            not_visited.append(x)

        for chromosome in chromosomes:
            for i in range(-1, len(chromosome) - 1):
                add(chromosome[i], -chromosome[i + 1])
                add(-chromosome[i + 1], chromosome[i])

        return cls(al, not_visited)

    def __str__(self):
        keys = set(self.al.keys())
        cycles = []
        while keys:
            current = keys.pop()
            cycle = [current]
            while self.al[current] != -cycle[0]:
                current = -self.al[current]
                cycle.append(current)
                keys.remove(current)
                keys.remove(-current)
            keys.remove(-cycle[0])
            cycles.append(cycle)
        return ''.join('(' + ' '.join(['{0:+d}'.format(block) for block in cycle]) + ')' for cycle in cycles)


def steps(g1, g2):
    yield str(g1)
    while g1.not_visited:
        current = g1.not_visited.pop()
        if g1[current] != g2[current]:
            a, b, c, d = g1[current], current, g1[g2[current]], g2[current]
            g1[g1[g2[current]]] = a
            g1[g2[current]] = b
            g1[g1[current]] = c
            g1[current] = d
            yield str(g1)


def main():
    g1 = Genome.from_string('(+1 -2 -3 +4)')
    g2 = Genome.from_string('(+1 +2 -4 -3)')

    print('\n'.join(steps(g1, g2)))


if __name__ == "__main__":
    main()

'''
output
(+1 -2 -3 +4)
(+1 -2 +3 +4)
(+1 -2 -4 -3)
(+1 +2 -4 -3)
'''
