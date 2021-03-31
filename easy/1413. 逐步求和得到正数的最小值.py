# coding=utf-8
class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 前缀和列表
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        if min(nums) > 0:
            return 1
        else:
            return 1 - min(nums)



if __name__ == '__main__':
    obj = Solution()
    nums = [-3, 2, -3, 4, 2] # [-3, -1, -4, 0, 2]
    # nums = [1, 2, 3]
    print obj.minStartValue(nums)