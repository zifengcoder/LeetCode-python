import collections


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        print dict(collections.Counter(barcodes)).items()
        stack = [sorted(dict(collections.Counter(barcodes)).items(), key=lambda x: (x[1], x[0]), reverse=True)[0][0]]
        count = len(barcodes)
        while len(stack) != count:
            data = sorted(dict(collections.Counter(barcodes)).items(), key=lambda x: (x[1], x[0]), reverse=True)
            for i in data:
                if stack and stack[-1]!=i[0]:
                    stack.append(i[0])
                    barcodes.remove(i[0])
                    break
        return stack


if __name__ == '__main__':
    obj = Solution()
    barcodes = [1,1,1,2,2,2]
    print obj.rearrangeBarcodes(barcodes)