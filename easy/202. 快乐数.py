class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        print n
        if n == 1:
            return True
        elif n>2**31-1 or n == 4:
            return False
        sum = 0
        for i in str(n):
            sum += int(i)**2
        return self.isHappy(sum)

    def isHappy2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        stack = []
        stack.append(n)
        while True:
            sum = 0
            for i in str(stack[-1]):
                sum += int(i) ** 2
            stack.append(sum)
            if sum == 1:
                return True
            elif len([i for i in stack if i==sum])>=2:
                return False


if __name__ == '__main__':
    obj = Solution()
    print obj.isHappy2(19)