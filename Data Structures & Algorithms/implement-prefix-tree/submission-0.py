class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for i in range(len(word)):
            if word[i] not in cur_node.children:
                cur_node.children[word[i]] = PrefixNode()
            cur_node = cur_node.children[word[i]]
        cur_node.eow = True

    def search(self, word: str) -> bool:
        cur_node = self.root
        for i in range(len(word)):
            if word[i] not in cur_node.children:
                return False
            cur_node = cur_node.children[word[i]]
        return cur_node.eow

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for i in range(len(prefix)):
            if prefix[i] not in cur_node.children:
                return False
            cur_node = cur_node.children[prefix[i]]
        return True
        
class PrefixNode:

    def __init__(self):
        self.children = {}
        self.eow = False