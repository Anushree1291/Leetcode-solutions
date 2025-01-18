class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
        root.endOfWord = True
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        trie = Trie()
        
        for word in strs:
            trie.insert(word)
            
        root = trie.root
        res = ''
        while root:
            if len(root.children) > 1 or root.endOfWord:
                return res
            
            key = list(root.children)[0]
            res += key
            
            root = root.children[key]
        return res