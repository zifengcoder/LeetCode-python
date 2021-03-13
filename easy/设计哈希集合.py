class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashSet = set()


    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashSet.add(key)


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hashSet:
            self.hashSet.remove(key)


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.hashSet:
            return True
        else:
            return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)