class Node:
    def __init__(self):
        self.children = {}

    def add_child(self, label, child):
        self.children[label] = child


def create_suffix_trie(text):
    root = Node()
    for j in range(len(text)):
        pattern = text[j:]
        curr = root
        for i in pattern:
            if i in curr.children:
                curr = curr.children[i]
            else:
                new = Node()
                curr.add_child(i, new)
                curr = new
    return root


def get_longest(root):
    edges = []

    def in_order(curr, edge):
        for label, child in curr.children.items():
            if len(curr.children) > 1:
                edges.append(edge)
            in_order(child, edge + label)

    in_order(root, '')
    return max(edges, key=lambda x: len(x))


def main(text):
    root = create_suffix_trie(text + '$')
    print(get_longest(root))


if __name__ == "__main__":
    main("ATATCGTTTTATCGTT")

'''
Given: A string Text.
Return: A longest substring of Text that appears in Text more than once. (Multiple solutions may exist, in which case 
you may return any one.)
Output:
TATCGTT
'''
