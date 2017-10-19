import numpy as np

SEP = '--------'


def distortion(centers, data):
    def distances(point):
        def distance(center):
            return np.linalg.norm(center - point) ** 2

        return np.min(np.apply_along_axis(distance, -1, centers))

    return np.sum(np.apply_along_axis(distances, -1, data)) / data.shape[0]


def main(m, centers_and_data_as_string):
    centers_as_string, data_as_string = centers_and_data_as_string.split(SEP)
    centers = np.fromstring(centers_as_string, sep=' ').reshape(-1, m)
    data = np.fromstring(data_as_string, sep=' ').reshape(-1, m)
    print('{:.3f}'.format(distortion(centers, data)))


if __name__ == '__main__':
    main(2, '''2.31 4.55
5.96 9.08
--------
3.42 6.03
6.23 8.25
4.76 1.64
4.47 4.33
3.95 7.61
8.93 2.97
9.74 4.03
1.73 1.28
9.72 5.01
7.27 3.77''')

'''
Given: Integer m, followed by a set of centers Centers and a set of points Data.
Return: The squared error distortion Distortion(Data, Centers).
Output:
18.246
'''
