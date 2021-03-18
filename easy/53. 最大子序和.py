class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tempSum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            tempSum = max(tempSum+nums[i], nums[i])
            maxSum = max(maxSum, tempSum)
        return maxSum