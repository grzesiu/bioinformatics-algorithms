class Node:
    def __init__(self):
        self.s_ids = set()
        self.children = {}

    def add_child(self, label, child, s_id):
        self.children[label] = child
        self.s_ids.add(s_id)


def add_to_suffix_trie(root, s, s_id):
    for j in range(len(s)):
        pattern = s[j:]
        curr = root
        for i in pattern:
            if i in curr.children:
                curr = curr.children[i]
            else:
                new = Node()
                curr.add_child(i, new, s_id)
                curr = new


def get_longest(root):
    edges = []

    def traverse(curr, edge):
        for label, child in curr.children.items():
            if len(curr.s_ids) == 2:
                edges.append(edge)
            traverse(child, edge + label)

    traverse(root, '')
    return max(edges, key=lambda x: len(x))


def main(text):
    s1, s2 = text.split()
    root = Node()
    add_to_suffix_trie(root, s1 + '$', 1)
    add_to_suffix_trie(root, s2 + '#', 2)
    print(get_longest(root))


if __name__ == "__main__":
    main('''TCGGTAGATTGCGCCCACTC
AGGGGCTCGCAGTGTAAGAA''')

'''
Find the longest substring shared by two strings.
Given: Strings Text1 and Text2.
Return: The longest substring that occurs in both Text1 and Text2. (Multiple solutions may exist, in which case you may
return any one.)
Output:
AGA
'''
