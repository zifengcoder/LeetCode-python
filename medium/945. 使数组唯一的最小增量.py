import collections


class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        while len(collections.Counter(A)) != len(A):
            for k, v in dict(collections.Counter(A)).items():
                if v != 1:
                    A[A.index(k)] += 1
                    count += 1
                    continue
        print A
        return count


    def minIncrementForUnique2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 1:
            return 0
        b = sorted(A)
        count = 0
        for i in range(len(b)):
            if i == len(b) - 1:
                if b[i - 1] < b[i]:
                    break
                else:
                    while b[i - 1] > b[i]:
                        b[i] += 1
                        count += 1
            while b[i + 1] <= b[i]:
                b[i + 1] += 1
                count += 1
        return count


    def minIncrementForUnique3(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        count = 0
        for i in range(1, len(A)):
            if A[i]<=A[i-1]:
                count += A[i-1] - A[i] + 1
                A[i] = A[i-1] +1
        return count



if __name__ == '__main__':
    obj = Solution()
    # a = [1, 1, 1, 1, 1] # [1, 2, 2] [3,2,1,2,1,7] [1, 1, 2, 2, 7]
    a = [5,8, 8, 10, 10, 17]
    print obj.minIncrementForUnique3(a)
    # print obj.minIncrementForUnique2(a)