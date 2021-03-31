from collections import Counter
from itertools import combinations


class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        stack = []
        for i in puzzles:
            count = 0
            for j in words:
                flag = False
                flag2 = False
                if i[0] in j:
                    flag = True
                    flag2 = True
                    for k in j:
                        if k not in i:
                            flag2 = False
                            break
                if flag and flag2:
                    count += 1
            stack.append(count)
        return stack


    def findNumOfValidWords2(self, words, puzzles):
        counter = Counter(filter(lambda x: len(x) <= 7, map(frozenset, words)))
        ans = [0] * (len(puzzles))
        for index, puzzle in enumerate(puzzles):
            for comb in list(map(lambda i: combinations(puzzle[1:], i), range(7))):
                data = [counter[frozenset((puzzle[0],) + ele)] for ele in comb]
                ans[index] += sum(data)
        return ans


if __name__ == '__main__':
    obj = Solution()
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
    print obj.findNumOfValidWords2(words, puzzles)