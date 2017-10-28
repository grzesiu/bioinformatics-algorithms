class Node:
    def __init__(self, *args):
        self.s_ids = set(args)
        self.children = {}

    def add_child(self, label, child):
        self.children[label] = child


def add_to_suffix_trie(root, s, s_id):
    for j in range(len(s)):
        pattern = s[j:]
        curr = root
        for i in pattern:
            if i in curr.children:
                curr.s_ids.add(s_id)
                curr = curr.children[i]
                curr.s_ids.add(s_id)
            else:
                new = Node(s_id)
                curr.add_child(i, new)
                curr.s_ids.add(s_id)
                curr = new


def get_shortest(root):
    queue = [(root, '')]
    while queue:
        curr, path = queue.pop(0)
        if len(curr.s_ids) == 1 and next(iter(curr.s_ids)) == 1:
            return path
        else:
            for label, child in curr.children.items():
                queue.append((child, path + label))


def main(text):
    s1, s2 = text.split()
    root = Node(1, 2)
    add_to_suffix_trie(root, s1, 1)
    add_to_suffix_trie(root, s2, 2)

    print(get_shortest(root))


if __name__ == "__main__":
    main('''CCAAGCTGCTAGAGG
CATGCTGGGCTGGCT''')

'''
Find the shortest substring of one string that does not appear in another string.
Given: Strings Text1 and Text2.
Return: The shortest substring of Text1 that does not appear in Text2. (Multiple solutions may exist, in which case you 
may return any one.)
Output:
AA
'''
