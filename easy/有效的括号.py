class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if stack:
                temp = stack[-1] + i
                if temp == '{}' or temp == '()' or temp == '[]':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True

    def isValid2(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''


if __name__ == '__main__':
    obj = Solution()
    s = "()[]{}" # "{[]}"  "([)]"
    print obj.isValid(s)