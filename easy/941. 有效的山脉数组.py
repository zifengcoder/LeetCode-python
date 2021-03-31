

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) >2:
            if sorted(arr) == arr or sorted(arr, reverse=True) == arr:
                return False
            a = arr[:arr.index(max(arr))]
            b = arr[arr.index(max(arr)):]
            if a == sorted(set(a)) and b == sorted(set(b), reverse=True):
                return True
            return False
        else:
            return False



if __name__ == '__main__':
    obj = Solution()
    arr = [3, 5, 5]
    print obj.validMountainArray(arr=arr)