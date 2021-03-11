# coding=utf-8
class Solution1(object):
    def removeKdigits(self, num, k):
        ''''''
        stack = []
        # 去掉 k 个数字保留最小的数字
        remain = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'


class Solution:
    def maxNumber(self, nums1, nums2, k):

        def pick_max(nums, k):
            '''
            去掉 len(nums)-k 个值保证数值最大
            :param nums:
            :param k:
            :return:
            '''
            stack = []
            # 去掉 drop 个数字保留最大的数字
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(A, B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger[0])
                bigger.pop(0)
            return ans
        return max(merge(pick_max(nums1, i), pick_max(nums2, k-i)) for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2))


if __name__ == '__main__':
    obj = Solution()
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    print obj.maxNumber(nums1, nums2, k)