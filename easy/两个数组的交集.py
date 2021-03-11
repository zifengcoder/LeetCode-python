# coding=utf-8
import collections


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp = []
        for i in nums1[:]:
            if i in nums2[:]:
                temp.append(i)
                nums1.remove(i)
                nums2.remove(i)
        return temp

    def intersect2(self, nums1, nums2):
        dct1 = collections.Counter(nums1)  ##  对dct1和dct2进行转换
        dct2 = collections.Counter(nums2)
        dct = dct1 & dct2  ## 取dct1和dct2的交集
        print dct
        print list(dct)
        return list(dct.elements())  # .elements()是一个迭代器


if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    obj = Solution()
    print obj.intersect2(nums1, nums2)
