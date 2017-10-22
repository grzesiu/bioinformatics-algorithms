import numpy as np


class DM:
    def __init__(self, n, distances):
        self.n = n
        self.distances = distances
        np.fill_diagonal(self.distances, np.inf)
        self.clusters = [Cluster([point]) for point in range(n)]

    @classmethod
    def from_str(cls, dm_as_str):
        n_as_str, distances_as_str = dm_as_str.split('\n', 1)
        n = int(n_as_str)
        distances = np.fromstring(distances_as_str, sep=' ').reshape(n, n)
        return cls(n, distances)

    def get_new(self, id1, id2):
        c1 = self.clusters[id1]
        c2 = self.clusters[id2]
        new_d = (self.distances[id1, :] * c1.weight + self.distances[id2, :] * c2.weight) / (
            c1.weight + c2.weight)
        new_d = new_d[new_d < np.inf]

        new_c = Cluster(c1.points + c2.points)
        return new_d, new_c

    def update_distances(self, new_d):
        self.distances = np.hstack((self.distances, new_d[:, np.newaxis]))
        new_d = np.append(new_d, np.inf)
        self.distances = np.vstack((self.distances, new_d[np.newaxis]))

    def merge(self):
        id1, id2 = self.get_min()
        new_d, new_c = self.get_new(id1, id2)

        del self[(id1, id2)]

        self.update_distances(new_d)
        self.clusters.append(new_c)

        return new_c.points

    def __delitem__(self, indices):
        self.distances = np.delete(self.distances, indices, axis=0)
        self.distances = np.delete(self.distances, indices, axis=1)
        self.clusters.pop(max(indices))
        self.clusters.pop(min(indices))

    def __len__(self):
        return len(self.clusters)

    def get_min(self):
        return np.unravel_index(np.argmin(self.distances), self.distances.shape)


class Cluster:
    def __init__(self, points):
        self.points = points

    @property
    def weight(self):
        return len(self.points)


def hc(dm):
    while len(dm) > 1:
        print(' '.join(map(str, (c + 1 for c in dm.merge()))))


def main(dm_as_str):
    dm = DM.from_str(dm_as_str)
    hc(dm)


if __name__ == '__main__':
    main('''7
    0.00 0.74 0.85 0.54 0.83 0.92 0.89
    0.74 0.00 1.59 1.35 1.20 1.48 1.55
    0.85 1.59 0.00 0.63 1.13 0.69 0.73
    0.54 1.35 0.63 0.00 0.66 0.43 0.88
    0.83 1.20 1.13 0.66 0.00 0.72 0.55
    0.92 1.48 0.69 0.43 0.72 0.00 0.80
    0.89 1.55 0.73 0.88 0.55 0.80 0.00''')

'''
Given: An integer n, followed by an nxn distance matrix.
Return: The result of applying HierarchicalClustering to this distance matrix (using Davg), with each newly created cluster listed on each line.
Output:
4 6
5 7
3 4 6
1 2
5 7 3 4 6
1 2 5 7 3 4 6
'''
