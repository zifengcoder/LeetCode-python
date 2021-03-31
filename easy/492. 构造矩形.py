import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        m = 0
        n = 0
        x = area
        sqrt = int(math.sqrt(area))
        for i in range(1, sqrt+1):
            l = i
            w = area/i
            if l*w == area and abs(l-w) <= x:
                x = abs(l-w)
                m = l
                n = w
        return [max(m, n), min(m, n)]


if __name__ == '__main__':
    obj = Solution()
    area = 4
    print obj.constructRectangle(area)