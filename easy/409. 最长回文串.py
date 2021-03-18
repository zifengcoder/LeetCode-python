import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if_single_str = False
        echo_len = 0
        if len(collections.Counter(s)) == 1:
            return len(s)
        for k, v in collections.Counter(s).items():
            if v % 2 == 0:
                echo_len += v
            elif v/2 >= 1:
                echo_len += 2*(v/2)
                if_single_str = True
            else:
                if_single_str = True
        if if_single_str:
            echo_len += 1
        return echo_len

    def longestPalindrome2(self, s):
        count = sum([2*(i/2) for i in collections.Counter(s).values()])
        return count if count==len(s) else count+1

if __name__ == '__main__':
    obj = Solution()
    s = 'sfsdfsdfdfd'
    print obj.longestPalindrome2(s)