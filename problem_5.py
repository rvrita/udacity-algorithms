from collections import defaultdict

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = defaultdict(TrieNode)
        
    def find_words(self, prefix):
        matches = []
        if self.is_word:
            matches += [prefix]
        for (char, node) in self.children.items():
            matches += node.find_words(prefix + char)

        return matches

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            node = node.children[char]

        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def match(self, prefix):
        ## Return all matching words in the tree
        node = self.find(prefix)
        if node:
            return node.find_words(prefix)
        else:
            return []

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


print(MyTrie.match("")) # Empty prefix - should return everything
print(MyTrie.match("ant"))
print(MyTrie.match("anth"))
print(MyTrie.match("f"))
print(MyTrie.match("fu"))
print(MyTrie.match("func"))
print(MyTrie.match("tri"))
print(MyTrie.match("trig"))
print(MyTrie.match("b")) # Doesn't exist - should return empty list
