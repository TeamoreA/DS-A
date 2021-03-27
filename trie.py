class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False

class Trie:
    def __init__(self):
        self.root_node = TrieNode()

    def insert(self, word):
        current_node = self.root_node

        for ch in word:
            node = current_node.children.get(ch)
            if node is None:
                node = TrieNode()
                current_node.children[ch] = node
            current_node = node
        current_node.end_of_string = True
        return word

    def search_string(self, word):
        root_node = self.root_node

        for ch in word:
            current_node = root_node.children.get(ch)
            if current_node is None:
                return False
            root_node = current_node

        if root_node.end_of_string:
            return True
        return False

    def delete(self, word):
        root = self.root_node
        i = 1
        for ch in word:
            kids = root.children

            current_node = kids.get(ch,)
            if current_node is None:
                del kids[ch]
                current_node.end_of_string = False
            elif current_node and i == len(word):
                current_node.end_of_string = False
            i += 1   
            root = current_node

        return word
            

trie = Trie()
print(trie.insert('APP'))
print(trie.insert('A'))
print(trie.insert('API'))
print(trie.insert('APIS'))
print(trie.search_string('APP'))
print(trie.delete('A'))
print(trie.search_string('A'))
