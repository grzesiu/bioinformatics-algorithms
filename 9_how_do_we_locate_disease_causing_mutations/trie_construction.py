class Node:
    def __init__(self, count):
        self.count = count
        self.children = {}

    def add_child(self, label, child):
        self.children[label] = child


def main(patterns):
    count = 0
    root = Node(count)
    for pattern in patterns.splitlines():
        curr = root
        for i in pattern:
            if i in curr.children:
                curr = curr.children[i]
            else:
                count += 1
                new = Node(count)
                print('{}->{}:{}'.format(curr.count, new.count, i))
                curr.add_child(i, new)
                curr = new


if __name__ == "__main__":
    main('''ATAGA
ATC
GAT''')

'''
Given: A collection of strings Patterns.
Return: The adjacency list corresponding to Trie(Patterns), in the following format. If Trie(Patterns) has n nodes, 
first label the root with 1 and then label the remaining nodes with the integers 2 through n in any order you like. Each
edge of the adjacency list of Trie(Patterns) will be encoded by a triple: the first two members of the triple must be 
the integers labeling the initial and terminal nodes of the edge, respectively; the third member of the triple must be 
the symbol labeling the edge.
Output:
0->1:A
1->2:T
2->3:A
3->4:G
4->5:A
2->6:C
0->7:G
7->8:A
8->9:T
'''
