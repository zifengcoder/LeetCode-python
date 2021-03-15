class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, value in enumerate(nums):
            y = target - value
            if abs(target)%2 == 0 and y == value:
                if len([i for i, x in enumerate(nums) if x == y]) == 2:
                    return [i for i, x in enumerate(nums) if x == y]
            elif y in nums:
                return [index, nums.index(y)]


    def twoSum2(nums, target):
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i, j]


    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for index, value in enumerate(nums):
            cp = target - value
            if cp in hashMap:
                return [hashMap[cp], index]
            else:
                hashMap[value] = index


if __name__ == '__main__':
    obj = Solution()
    # [0, 0]
    print obj.twoSum(nums=[-3,4,3,90], target=0)
