class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        s = n % 3
        m = n / 3
        if s == 1:
            result = 3 ** (m - 1) * (n - (m - 1) * 3)
        elif s == 0:
            result = 3 ** m
        else:
            result = 3 ** m * s
        return result

if __name__ == '__main__':
    obj = Solution()
    print obj.integerBreak(4)