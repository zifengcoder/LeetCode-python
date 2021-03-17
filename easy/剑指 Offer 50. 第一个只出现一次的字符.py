import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = dict(collections.Counter(s))
        for i in s:
            if count[i] == 1:
                return i
        return " "


if __name__ == '__main__':
    obj = Solution()
    s = 'leetcode'
    print obj.firstUniqChar(s)