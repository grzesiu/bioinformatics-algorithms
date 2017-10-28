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


def traverse(curr, edge):
    if not len(curr.children):
        print(edge)
    elif len(curr.children) == 1:
        label, child = next(iter(curr.children.items()))
        traverse(child, edge + label)
    else:
        if edge:
            print(edge)
        for label, child in curr.children.items():
            traverse(child, label)


def main(text):
    root = create_suffix_trie(text)
    traverse(root, '')


if __name__ == "__main__":
    main("ATAAATG$")

'''
Given: A string Text.
Return: The strings labeling the edges of SuffixTree(Text). (You may return these strings in any order.)
Output:
T
G$
AAATG$
A
T
G$
AAATG$
A
TG$
ATG$
G$
$
'''
