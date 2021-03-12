class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            return self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return min(self.stack)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()