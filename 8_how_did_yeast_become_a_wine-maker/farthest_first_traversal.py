import numpy as np


def find_distances(centers, point):
    def distance(center):
        return np.linalg.norm(center - point)

    return np.apply_along_axis(distance, -1, centers)


def find_min_distance_point(data, centers):
    max_distance_point = data[0]
    max_distance_point_min_distance = 0

    for current in data[1:]:
        current_min_distance = np.min(find_distances(centers, current))
        if current_min_distance > max_distance_point_min_distance:
            max_distance_point = current
            max_distance_point_min_distance = current_min_distance

    return max_distance_point


def find_centers(k, data):
    centers = [data[0]]
    find_min_distance_point(data, centers)

    while len(centers) < k:
        centers.append(find_min_distance_point(data, centers))

    return centers


def main(k, m, data_as_string):
    data = np.fromstring(data_as_string, sep=' ').reshape(-1, m)
    for center in find_centers(k, data):
        print(' '.join(map('{:.1f}'.format, center)))


if __name__ == '__main__':
    main(3, 2, '''0.0 0.0
5.0 5.0
0.0 5.0
1.0 1.0
2.0 2.0
3.0 3.0
1.0 2.0''')

'''
Given: Integers k and m followed by a set of points Data in m-dimensional space.
Return: A set Centers consisting of k points (centers) resulting from applying FarthestFirstTraversal(Data, k), where the first point from Data is chosen as the first center to initialize the algorithm.
Output:
0.0 0.0
5.0 5.0
0.0 5.0
'''
