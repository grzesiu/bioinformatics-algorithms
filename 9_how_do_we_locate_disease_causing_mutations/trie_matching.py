class Node:
    def __init__(self):
        self.children = {}

    def add_child(self, label, child):
        self.children[label] = child


def create_trie(patterns):
    root = Node()
    for pattern in patterns:
        curr = root
        for i in pattern:
            if i in curr.children:
                curr = curr.children[i]
            else:
                new = Node()
                curr.add_child(i, new)
                curr = new
    return root


def prefix_trie_match(i, text, root):
    curr = root
    while True:
        if i < len(text) and text[i] in curr.children:
            curr = curr.children[text[i]]
            i += 1
        elif not curr.children:
            return True
        else:
            return False


def trie_match(text, root):
    for i in range(len(text)):
        if prefix_trie_match(i, text, root):
            print(i, end=' ')


def main(data_as_str):
    text, patterns = data_as_str.split('\n', 1)
    root = create_trie(patterns.splitlines())
    trie_match(text, root)


if __name__ == "__main__":
    main('''AATCGGGTTCAATCGGGGT
ATCG
GGGT''')

'''
Given: A string Text and a collection of strings Patterns.
Return: All starting positions in Text where a string from Patterns appears as a substring.
Output:
1 4 11 15
'''
