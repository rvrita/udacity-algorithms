from collections import defaultdict

## Represents a single node in the Trie
class RouteTrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.handler = None
        self.children = defaultdict(RouteTrieNode)


## The Trie itself containing the root node and insert/find functions
class RouteTrie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = RouteTrieNode()

    def insert(self, parts, handler):
        ## Add a path to the Trie
        node = self.root
        for part in parts:
            node = node.children[part]

        node.handler = handler

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well
        self.trie = RouteTrie()
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        parts = self.split_path(path)
        self.trie.insert(parts, handler)

    def lookup(self, path):
        parts = self.split_path(path)
        node = self.trie.find(parts)
        if node and node.handler:
            return node.handler

        return self.not_found_handler

    def split_path(self, path):
        return ["root"] + list(filter(lambda x: x != '', path.split('/')))


# Test cases

router = Router("Not Found handler") # create the router
router.add_handler("/home/about", "About handler")  # add a route
router.add_handler("/home/", "Home handler")  # add a route with trailing slash

# some lookups with the expected output
print(router.lookup("/")) # should print 'Not Found handler'
print(router.lookup("/home")) # should print 'Home handler'
print(router.lookup("/home/about")) # should print 'About handler'
print(router.lookup("/home/about/")) # should print 'About handler'
print(router.lookup("/home///about/")) # should print 'About handler'
print(router.lookup("/home/about/me")) # should print 'Not Found handler'

router.add_handler("/", "Root handler")
print(router.lookup("/")) # should print 'Root handler'
print(router.lookup("")) # should print 'Root handler'
