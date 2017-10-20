from collections import defaultdict

import numpy as np


def find_closest_center(centers, point):
    def distance(center):
        return np.linalg.norm(center - point)

    return np.argmin(np.apply_along_axis(distance, -1, centers))


def centers_to_clusters(centers, points):
    clusters = defaultdict(list)

    def assign_to_center(point):
        closest_center = find_closest_center(centers, point)
        clusters[closest_center].append(point)

    np.apply_along_axis(assign_to_center, -1, points)
    return clusters


def clusters_to_centers(clusters):
    return np.array([np.average(np.array(cluster), axis=0) for cluster in clusters.values()])


def find_centers(k, points):
    prev_centers = None
    centers = points[:k]
    while np.any(centers != prev_centers):
        prev_centers = centers
        clusters = centers_to_clusters(prev_centers, points)
        centers = clusters_to_centers(clusters)

    return centers


def main(k, m, points_as_string):
    points = np.fromstring(points_as_string, sep=' ').reshape(-1, m)
    for center in find_centers(k, points):
        print(' '.join(map('{:.3f}'.format, center)))


if __name__ == '__main__':
    main(2, 2, '''1.3 1.1
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
Given: Integers k and m followed by a set of points Data in m-dimensional space.
Return: A set Centers consisting of k points (centers) resulting from applying the Lloyd algorithm to Data and Centers, where the first k points from Data are selected as the first k centers.
Output:
1.800 2.867
1.060 1.140
'''
