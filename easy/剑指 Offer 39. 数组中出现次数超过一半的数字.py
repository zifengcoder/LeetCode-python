import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = dict(collections.Counter(nums))
        for i in nums:
            if count[i]>len(nums)/2:
                return i