class Node(object):
    def __init__(self):
        self.flag = False
        self.sub_node = {}
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for s in word:
            if s not in current.sub_node:
                current.sub_node[s] = Node()
                current = current.sub_node[s]
            else:
                current = current.sub_node[s]
        current.flag = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for s in word:
            if s in curr.sub_node:
                curr = curr.sub_node[s]
            else:
                return False
        return curr.flag

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for s in prefix:
            if s in curr.sub_node:
                curr = curr.sub_node[s]
            else:
                return False
        return True

    '''
    def delete(self,world):
        if not self.search():
            return False
        pre = curr
        for s in word:
            if len(curr.sub_node[s].sub_node.keys())==1:
                flag_pre = pre
                flag_c = s
            pre = curr.sub_node[s]
        del flag_pre[flag_c]
    '''
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
