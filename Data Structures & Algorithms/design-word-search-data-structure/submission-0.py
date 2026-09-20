class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.eow = True

    def search(self, word: str) -> bool:
        cur = self.root
        return self.search_from_node(cur, word)
    
    def search_from_node(self, node, word):
        for i in range(len(word)):
            c = word[i]
            if c=='.':
                return any([self.search_from_node(new_node, word[i+1:]) for new_node in node.children.values()])
            elif c not in node.children:
                return False
            else:
                node = node.children[c]
        return node.eow

class Node:
    def __init__(self):
        self.children = {}
        self.eow = False