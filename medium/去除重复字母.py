# coding=utf-8
import collections

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        建立一个字典。其中 key 为 字符 c，value 为其出现的剩余次数。
        从左往右遍历字符串，每次遍历到一个字符，其剩余出现次数 - 1.
        对于每一个字符，如果其对应的剩余出现次数大于 1，我们可以选择丢弃（也可以选择不丢弃），否则不可以丢弃。
        是否丢弃的标准和上面题目类似。如果栈中相邻的元素字典序更大，那么我们选择丢弃相邻的栈中的元素。

        :type s: str
        :rtype: str
        """
        stack = []
        counter =  collections.Counter(s)
        for i in s:
            if i not in stack:
                while stack and i<stack[-1] and counter[stack[-1]]>0:
                    stack.pop()
                stack.append(i)
            counter[i] -= 1
        return "".join(stack)


    def removeDuplicateLetters2(self, s):
        stack = []
        seen = set()
        remain_counter = collections.Counter(s)

        for c in s:
            if c not in seen:
                while stack and c < stack[-1] and  remain_counter[stack[-1]] > 0:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)


if __name__ == '__main__':
    obj = Solution()
    s = "cbacdcbc"
    print obj.removeDuplicateLetters2(s)