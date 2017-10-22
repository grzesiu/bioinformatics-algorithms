import numpy as np


def centers_to_clusters(beta, points, centers):
    diffs = points[:, np.newaxis] - centers
    distances = np.sqrt(np.sum(np.square(diffs), axis=-1))
    hidden = np.exp(-beta * distances)
    hidden /= np.sum(hidden, axis=-1)[:, np.newaxis]
    return hidden


def clusters_to_centers(points, hidden):
    weighted = points[:, np.newaxis] * hidden[..., np.newaxis]
    return np.sum(weighted, axis=0) / np.sum(hidden, axis=0)[:, np.newaxis]


def find_centers(k, beta, points):
    centers = points[:k]
    for _ in range(100):
        hidden = centers_to_clusters(beta, points, centers)
        centers = clusters_to_centers(points, hidden)
    return centers


def main(k, m, beta, points_as_string):
    points = np.fromstring(points_as_string, sep=' ').reshape(-1, m)
    for center in find_centers(k, beta, points):
        print(' '.join(map('{:.3f}'.format, center)))


if __name__ == '__main__':
    main(2, 2, 2.7, '''1.3 1.1
1.3 0.2
0.6 2.8
3.0 3.2
1.2 0.7
1.4 1.6
1.2 1.0
1.2 1.1
0.6 1.5
1.8 2.6
1.2 1.3
1.2 1.0
0.0 1.9''')

'''
Given: Integers k and m, followed by a stiffness parameter β, followed by a set of points Data in m-dimensional space.
Return: A set Centers consisting of k points (centers) resulting from applying the soft k-means clustering algorithm. Select the first k points from Data as the first centers for the algorithm and run the algorithm for 100 steps. Results should be accurate up to three decimal places.
1.662 2.623
1.075 1.148
'''
