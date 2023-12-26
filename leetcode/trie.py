class Trie:
    END_OF_STRING = object()

    def __init__(self):
        self.state = {}

    def insert(self, word: str) -> None:
        current_trie = self.state
        for char in word:
            if char not in current_trie:
                current_trie[char] = {}

            current_trie = current_trie[char] # advance to next layer of trie/dict

        current_trie[Trie.END_OF_STRING] = True

    def search(self, word: str) -> bool:
        current_trie = self.state
        for char in word:
            if char not in current_trie:
                return False

            current_trie = current_trie[char] # advance to next layer of trie/dict

        # Check if the last entered trie also has end of string flag or not. 
        return current_trie.get(Trie.END_OF_STRING, False)

    def startsWith(self, prefix: str) -> bool:
        current_trie = self.state
        for char in prefix:
            if char not in current_trie:
                return False
            current_trie = current_trie[char] # advance to next layer of trie/dict

        return True #regardless of whether its the end or not

# Your Trie object will be instantiated and called as such:

words = ["hi", "hello", "hey", "take"]
obj = Trie()
for word in words:
    obj.insert(word)

print(obj.search("hi"))
print(obj.search("hello"))
print(obj.search("hell"))
print(obj.startsWith("t"))
print(obj.startsWith("hell"))