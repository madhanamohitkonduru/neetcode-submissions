class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word):
        curr = self.root
        q = collections.deque()
        q.append((0, curr))

        while q:
            i, node = q.pop()
            if i == len(word):
                if node.end==True:
                    return True
                continue
            c = word[i]
            if c in node.children:
                q.append((i+1, node.children[c]))
            elif c == ".":
                for child in node.children.values():
                    q.append((i+1, child))
        return False