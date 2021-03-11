class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = 1
        y = 0
        for i in s:
            if i == 'A':
                x = 2*x + y
            else:
                y = 2*y + x
        return x+y

if __name__ == '__main__':
    obj = Solution()
    s = "AB"
    print obj.calculate(s)