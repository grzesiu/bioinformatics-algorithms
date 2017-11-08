from collections import defaultdict


class Node:
    def __init__(self):
        self.i = None
        self.parent = None
        self.color = None
        self.children = []


class G:
    def __init__(self, nodes, colors):
        self.nodes = nodes
        self.colors = colors
        self.color(self.get_root())

    def get_root(self):
        for node in self.nodes.values():
            if node.parent is None:
                return node

    def color(self, node):
        children_colors = set()
        if node.children:
            for child in node.children:
                c = self.color(child)
                children_colors.add(c)
            if len(children_colors) == 1:
                node.color = children_colors.pop()
            else:
                node.color = 'purple'
        else:
            node.color = self.colors[node.i]
        return node.color

    def __str__(self):
        return '\n'.join(['{}: {}'.format(node.i, node.color) for node in self.nodes.values()])

    @classmethod
    def from_str(cls, g_as_string):
        al_as_string, labels_as_string = g_as_string.split('-\n')

        def parse_color(as_str):
            n, c = as_str.split(': ')
            return int(n), c

        colors = dict(parse_color(pair) for pair in labels_as_string.strip().split('\n'))
        nodes = defaultdict(Node)
        al_as_string = al_as_string.strip().split('\n')
        al_as_string = (row.split(' -> ') for row in al_as_string)

        def to_list(list_as_string):
            l = list_as_string.strip('{}')
            return list(map(int, l.split(','))) if l else []

        for k, v in al_as_string:
            parent_id, child_ids = int(k), to_list(v)
            nodes[parent_id].i = parent_id
            for child_id in child_ids:
                nodes[child_id].i = child_id
                nodes[child_id].parent = nodes[parent_id]
                nodes[parent_id].children.append(nodes[child_id])
        return G(nodes, colors)


def main(g_as_string):
    g = G.from_str(g_as_string)
    print(g)


if __name__ == "__main__":
    main('''0 -> {}
1 -> {}
2 -> 0,1
3 -> {}
4 -> {}
5 -> 3,2
6 -> {}
7 -> 4,5,6
-
0: red
1: red
3: blue
4: blue
6: red''')

'''
Color the internal nodes of a suffix tree given colors of the leaves.
Given: An adjacency list, followed by color labels for leaf nodes.
Return: Color labels for all nodes, in any order.
Output:
0: red
1: red
2: red
3: blue
4: blue
5: purple
6: red
7: purple
'''
