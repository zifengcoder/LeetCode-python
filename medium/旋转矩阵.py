# coding=utf-8
class Solution(object):
    def rotate(self, matrix):
        """
        先对角反转，再转置
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for k in matrix:
            k.reverse()
        return matrix

    def rotate2(self, matrix):
        """
        先上下翻转，再zip取转置。
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        print matrix
        print matrix[::-1]
        matrix[::] = zip(*matrix[::-1])
        return matrix



if __name__ == '__main__':
    obj = Solution()
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    # matrix = [[1,2],[3,4]]
    print obj.rotate(matrix)