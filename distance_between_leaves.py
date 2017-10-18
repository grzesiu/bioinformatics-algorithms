from collections import defaultdict


def get_distances(leaves, al):
    root = next(iter(al))
    paths = {}
    visited = [False] * len(al)

    def dfs(path):
        (parent, root_to_parent) = path[-1]
        for child, parent_to_child in al[parent]:
            if not visited[child]:
                visited[child] = True
                child_path = list(path)
                child_path.append((child, root_to_parent + parent_to_child))
                paths[child] = child_path
                dfs(child_path)

    def lca(path1, path2):
        c = 0
        while path1[c + 1] == path2[c + 1]:
            c += 1
        return path1[c][1]

    dfs([(root, 0)])

    distances = [[0] * leaves for _ in range(leaves)]
    for j in range(leaves):
        for i in range(leaves):
            if i != j:
                common_distance = lca(paths[i], paths[j])
                distances[j][i] = paths[i][-1][1] + paths[j][-1][1] - 2 * common_distance

    return distances


def parse(al_as_string):
    al = defaultdict(list)
    for edge in al_as_string.splitlines():
        f, td = edge.split('->')
        t, d = td.split(':')
        f, t, d = map(int, (f, t, d))
        al[f].append((t, d))
    return al


def main():
    n = 4
    al_as_string = '''0->4:11
1->4:2
2->5:6
3->5:7
4->0:11
4->1:2
4->5:4
5->4:4
5->3:7
5->2:6'''

    al = parse(al_as_string)
    distances = get_distances(n, al)
    for row in distances:
        print(" ".join(map(str, row)))


if __name__ == '__main__':
    main()

'''
Compute the distances between leaves in a weighted tree.
Given: An integer n followed by the adjacency list of a weighted tree with n leaves.
Return: A space-separated n x n (di, j), where di, j is the length of the path between leaves i and j.

output
0   13  21  22
13  0   12  13
21  12  0   13
22  13  13  0
'''
